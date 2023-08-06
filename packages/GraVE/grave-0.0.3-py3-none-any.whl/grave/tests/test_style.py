import pytest

from grave import style
from grave.style import (apply_style, 
                         generate_edge_styles,
                         generate_node_styles,
                         use_attributes,
                         default_node_style,
                         default_edge_style,
                         _VALID_NODE_STYLE,
                         _VALID_EDGE_STYLE,
                         _ALL_STYLE_KEYS)

def test_generate_node_styles_callable(barbell_network):

    def style_func(attrs):
        return {'color': 'red'}

    node_styles = generate_node_styles(barbell_network,
                                       style_func)
    
    expected = default_node_style()
    expected['color'] = 'red'
    for node, style in node_styles.items():
        assert node in barbell_network
        assert style == expected


def test_generate_node_styles_dict(barbell_network):
    updated = {'color': 'red'}

    node_styles = generate_node_styles(barbell_network,
                                       updated)

    expected = default_node_style()
    expected['color'] = 'red'
    for node, style in node_styles.items():
        assert node in barbell_network
        assert style == expected

def test_generate_node_style_typerror(barbell_network):
    with pytest.raises(TypeError):
        node_styles = generate_node_styles(barbell_network,
                                       'red')


def test_generate_edge_styles_callable(barbell_network):
    def style_func(attrs):
        return {'color': 'red'}

    edge_styles = generate_edge_styles(barbell_network,
                                       style_func)
    
    expected = default_edge_style()
    expected['color'] = 'red'
    for edge, style in edge_styles.items():
        assert edge in barbell_network.edges
        assert style == expected


def test_generate_edge_styles_dict(barbell_network):
    style = {'color': 'red'}

    edge_styles = generate_edge_styles(barbell_network,
                                       style)

    expected = default_edge_style()
    expected['color'] = 'red'
    for edge, style in edge_styles.items():
        assert edge in barbell_network.edges
        assert style == expected


def test_generate_edge_style_typerror(barbell_network):
    with pytest.raises(TypeError):
        edge_styles = generate_edge_styles(barbell_network,
                                           'red')

@pytest.mark.parametrize('style_key', _ALL_STYLE_KEYS)
def test_use_style_attributes_default(style_key, barbell_network):
    for node, node_attr in barbell_network.nodes.data():
        node_attr[style_key] = 'TEST'

    node_styles = generate_node_styles(barbell_network,
                                       use_attributes())

    for node, style in node_styles.items():
        assert node in barbell_network
        assert style[style_key] == 'TEST'


def test_use_style_attributes_filter_single(barbell_network):
    for node, node_attr in barbell_network.nodes.data():
        for style_key in _ALL_STYLE_KEYS:
            node_attr[style_key] = 'TEST'

    node_styles = generate_node_styles(barbell_network,
                                       use_attributes('color'))

    expected = default_node_style()
    expected['color'] = 'TEST'
    for node, style in node_styles.items():
        assert node in barbell_network
        assert style == expected


def test_use_style_attributes_filter_list(barbell_network):
    for node, node_attr in barbell_network.nodes.data():
        for style_key in _ALL_STYLE_KEYS:
            node_attr[style_key] = 'TEST'

    node_styles = generate_node_styles(barbell_network,
                                       use_attributes(['color', 'shape']))
    expected = default_node_style()
    expected['color'] = 'TEST'
    expected['shape'] = 'TEST'
    for node, style in node_styles.items():
        assert node in barbell_network
        assert style == expected
