'''
# importreqs

A simple Python lib for extracting reqs.txt from currently
imported libs in the context.
'''
import sys
import os
try:
    from pip import FrozenRequirement, get_installed_distributions
except Exception as e:
    from pip._internal import get_installed_distributions
    from pip._internal.operations.freeze import FrozenRequirement


def build_reverse_package_file_map():
    package_file_map = {}
    for dist in get_installed_distributions():
        if not dist._provider.egg_info:
            continue
        record_file = '%s/RECORD' % dist._provider.egg_info
        sources_txt_file = '%s/SOURCES.txt' % dist._provider.egg_info
        target_file = None
        if os.path.exists(record_file):
            target_file = record_file
        elif os.path.exists(sources_txt_file):
            target_file = sources_txt_file
        if target_file:
            for line in open(target_file).readlines():
                line = line.strip().split(',')
                if not line:
                    continue
                line = line[0].strip()
                if line.endswith('.py'):
                    src_line = "%s/%s" % (dist._provider.module_path, line)
                    package_file_map[src_line] = dist
    return package_file_map


def build_reverse_package_name_map():
    package_name_map = {}
    for dist in get_installed_distributions():
        package_name_map[dist.project_name] = dist
    return package_name_map


def get_intersected_distributions(package_file_map=None, package_name_map=None):
    '''
    Get intersected sets between installed distributions and imported libs
    from current context.
    '''
    if package_file_map is None:
        package_file_map = build_reverse_package_file_map()
    if package_name_map is None:
        package_name_map = build_reverse_package_name_map()
    distributions = {}
    for name, module in sys.modules.items():
        dist_name = None
        if hasattr(module, '__file__'):
            dist = package_file_map.get(module.__file__)
            if dist:
                distributions[dist.project_name] = dist
        elif hasattr(module, '__package__'):
            package = (module.__package__ or '').strip()
            if package:
                if '.' in package:
                    pacakge = package.split('.')[0]
            if package not in distributions and package in package_name_map:
                distributions[package] = package_name_map[package]
    return distributions


def get_req_distributions():
    '''
    Get the distribution instances.
    '''
    intersected = get_intersected_distributions()
    for dist in intersected.values():
        dependency_links = []
        if dist.has_metadata('dependency_links.txt'):
            dependency_links = dist.get_metadata_lines('dependency_links.txt')
        frozen_dist = FrozenRequirement.from_dist(dist,
                                                 dependency_links)
        yield(frozen_dist)


def generate_reqs():
    '''
    Generate the content of reqs.txt.
    '''
    return ''.join([str(i) for i in get_req_distributions()])
