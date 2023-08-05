"""
Tools for parsing markdown docs.
"""
from bs4 import BeautifulSoup
from collections import defaultdict
from rundoc.block import DocBlock
from rundoc.commander import DocCommander
import json
import markdown
import markdown_rundoc.rundoc_code
import operator
import re

def generate_match_class(tags="", must_have_tags="", must_not_have_tags="",
    is_env=False, is_secret=False):
    """Generate match_class(class_name) function.

    Function match_class(class_name) is used to filter html classes that
    comply with tagging rules provided. Lists of tags are hash (#) separated
    strings. Example: "tag1#tag2#tag3".

    Args:
        tags (str): At least one tag must exist in class name.
        must_have_tags (str): All tags must exist in class name. Order is not
            important.
        must_not_have_tags (str): None of these tags may be found in the class
            name.
        is_env (bool): If set to True then match only class names that begin
            with environment tag, otherwise don't match them.
        is_secret (bool): If set to True then match only class names that begin
            with secret tag, otherwise don't match them.
    Returns:
        Function match_class(class_name).
    """
    def match_class(class_name):
        if not class_name: class_name = "" # avoid working with None
        if is_env and is_secret:
            raise Exception("Block can't be both env and secret.")
        only_env = re.compile("^env(iron(ment)?)?($|{}).*$".format(
            re.escape('#')))
        if is_env and not only_env.match(class_name):
            return False
        only_secrets = re.compile("^secrets?($|{}).*$".format(
            re.escape('#')))
        if is_secret and not only_secrets.match(class_name):
            return False
        code_block = re.compile("^(?!(env(iron(ment)?)?|secrets?)).*$")
        if not (is_env or is_secret) and not code_block.match(class_name):
            return False
        match_tags = re.compile("^.*(^|{s})({tags})({s}|$).*$".format(
            tags = '|'.join(list(filter(bool, tags.split('#')))),
            s = re.escape('#')))
        if tags and not match_tags.match(class_name):
            return False
        match_all_tags = re.compile(
            "^{}.*$".format(''.join('(?=.*(^|{s}){tag}($|{s}))'.format(
                s = re.escape('#'),
                tag = tag) for tag in list(
                    filter(bool, must_have_tags.split('#'))))))
        if must_have_tags and not match_all_tags.match(class_name):
            return False
        not_match_tags = re.compile("^(?!.*(^|{s})({tags})($|{s})).*$".format(
            tags = '|'.join(list(filter(bool,
                must_not_have_tags.split('#')))),
            s = re.escape('#')))
        if must_not_have_tags and not not_match_tags.match(class_name):
            return False
        return True
    return match_class

def parse_doc(input, tags="", must_have_tags="", must_not_have_tags="",
    light=False, **kwargs):
    """Parse code blocks from markdown file and return DocCommander object.

    Args:
        input (file): Readable file-like object pointing to markdown file.
        tags (str): Hash (#) separated list of tags. Markdown code block that
            contain at least one of them will be used.
        must_have_tags (str): Like 'tags' but require markdown code block to
            contain all of them (order not important).
        must_not_have_tags (str): Like 'tags' but require markdown code block
            to contain non of them.
        light (bool): Will use light backgrond color theme if set to True.
            Defaults to False.

    Returns:
        DocCommander object.
    """
    mkd_data = input.read()
    html_data = markdown.markdown(
        mkd_data,
        extensions = [ 'markdown_rundoc.rundoc_code' ]
        )
    soup = BeautifulSoup(html_data, 'html.parser')
    commander = DocCommander()
    # collect all elements with selected tags as classes
    match = generate_match_class(tags, must_have_tags, must_not_have_tags)
    code_block_elements = soup.findAll(name='code', attrs={"class":match,})
    for element in code_block_elements:
        class_name = element.get_attribute_list('class')[0]
        if class_name:
            tags_list = class_name.split('#')
            tags_list = list(filter(bool, tags_list)) # remove empty strings
            interpreter = tags_list[0]
            commander.add(element.getText(), interpreter, light, class_name)
    # get env blocks
    match = generate_match_class(tags, must_have_tags, must_not_have_tags,
        is_env=True)
    env_elements = soup.findAll(name='code', attrs={"class":match,})
    env_string = "\n".join([ x.string or '' for x in env_elements ])
    commander.env.import_string(env_string)
    # get secrets blocks
    match = generate_match_class(tags, must_have_tags, must_not_have_tags,
        is_secret=True)
    secrets_elements = soup.findAll(name='code', attrs={"class":match,})
    secrets_string = "\n".join([ x.string for x in secrets_elements ])
    commander.secrets.import_string(secrets_string)
    return commander

def parse_output(input, exact_timing=False, light=False, **kwargs):
    """Load json output, create and return DocCommander object.

    Each code block recorded in the otput will be parsed and only code from
    successful attempts will be turned into code blocks for new session. The
    goal is to use original or user modified inputs as a new script.

    Args:
        output (file): Readable file-like object.
        exact_timing (bool): NOT IMPLEMENTED YET!
            If True, a code block will be created for each run try
            and pause between blocks and tries will be calculated from the
            timestamps recorded in the file. The goal is to recreate all exact
            steps that users may have done. Defaults to False.
        light (bool): Will use light backgrond color theme if set to True.
            Defaults to False.

    Returns:
        DocCommander object.
    """
    output_data = input.read()
    data = json.loads(output_data)
    commander = DocCommander()
    for d in data['code_blocks']:
        doc_block = DocBlock(
            code=d['runs'][-1]['user_code'],
            interpreter=d['interpreter'],
            light=light,
            tags=d['tags']
            )
        commander.doc_blocks.append(doc_block)
    return commander

def get_tags(input):
    tag_dict = defaultdict(int)
    mkd_data = input.read()
    html_data = markdown.markdown(
        mkd_data,
        extensions = [ 'markdown_rundoc.rundoc_code' ]
        )
    soup = BeautifulSoup(html_data, 'html.parser')
    match = re.compile("^.+$")
    code_block_elements = soup.findAll(name='code', attrs={"class":match,})
    for element in code_block_elements:
        class_name = element.get_attribute_list('class')[0]
        if class_name:
            for tag in class_name.split('#'):
                tag_dict[tag] += 1
    sorted_tag_dict = sorted(tag_dict.items(), key=operator.itemgetter(1),
        reverse=True)
    return sorted_tag_dict

def print_blocks(input, tags="", must_have_tags="", must_not_have_tags="",
    light=False, pretty=False):
    commander = parse_doc(input, tags, must_have_tags, must_not_have_tags,
        light)
    if pretty:
        step = 0
        for block in commander.doc_blocks:
            step += 1
            print("{}. [{}] {}".format(step, block.interpreter, block.tags))
            print("=================")
            print(block)
            print("")
    else:
        print(json.dumps(commander.get_dict(), sort_keys=True, indent=4))

def print_clean_doc(input):
    mkd_data = input.read()
    print(
        re.sub(
            '(\\n```[^#:]*).*?(\\n.*?```\\n)',
            '\\1\\2',
            mkd_data,
            flags=re.DOTALL
            )
        )

