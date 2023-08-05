__version__ = '0.1.2'

import cleanlog
import requests
import tqdm

logger = cleanlog.ColoredLogger('snakespit')
BASE_URL = 'http://dohlee-bio.info:9193/%s/rule.smk'


def get_rules(tools, out=None):
    """
    Get template snakemake rules for the given tools.

    :param list tools: The name of tools. For example, ['samtools/sort', 'samtools/index'].
    :param str out: (Optional) Output file path. If not specified, the resulting snakemake rules
        will be printed to stdout so that user can redirect it output to the desired file.
    """
    rule_content = []
    warnings = []
    for tool in tqdm.tqdm(tools):
        tool = tool.strip('/')
        response = requests.get(BASE_URL % tool)

        if response.status_code == 200 and not response.text.startswith('404'):
            rule_content.append(response.text.replace('\r\n', '\n'))
        else:
            warnings.append('No rule for %s.' % rule)

    for warning in warnings:
        logger.warning(warning)

    if out is None:
        print('\n'.join(rule_content))
    else:
        with open(out, 'w') as outFile:
            print('\n'.join(rule_content), file=outFile)
