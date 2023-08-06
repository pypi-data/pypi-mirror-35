# -*- coding: utf-8 -*-
"""
test_api
~~~~~~~~

Test the core API functionality.

"""

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
import logging
import os
import re
import time

import pytest
import six

from chemspipy import ChemSpider, errors


logging.basicConfig(level=logging.WARN)
logging.getLogger('chemspipy').setLevel(logging.DEBUG)

# API key is retrieved from environment variables
CHEMSPIDER_API_KEY = os.environ['CHEMSPIDER_API_KEY']

# Chemspider instances with and without an API key
cs = ChemSpider(CHEMSPIDER_API_KEY)


def test_no_api_key():
    """Test ChemSpider cannot be initialized with no API key."""
    with pytest.raises(TypeError):
        ChemSpider()


def test_api_key():
    """Test API key is set correctly when initializing ChemSpider."""
    assert cs.api_key == CHEMSPIDER_API_KEY


def test_chemspider_repr():
    """Test ChemSpider object repr."""
    assert repr(cs) == 'ChemSpider()'


# Lookups

def test_get_datasources():
    """Test get_datasources returns the list of ChemSpider data sources."""
    datasources = cs.get_datasources()
    assert all(source in datasources for source in ['Wikipedia', 'ZINC', 'PubChem'])


# Records

def test_get_details():
    """Test get_details returns details for a record ID."""
    info = cs.get_details(6543)
    assert all(field in info for field in [
        'id', 'smiles', 'formula', 'averageMass', 'molecularWeight', 'monoisotopicMass', 'nominalMass',
        'commonName', 'referenceCount', 'dataSourceCount', 'pubMedCount', 'rscCount', 'mol2D'
    ])
    assert all(isinstance(info[field], float) for field in [
        'averageMass', 'molecularWeight', 'monoisotopicMass'
    ])
    assert isinstance(info['id'], int)
    assert all(isinstance(info[field], six.text_type) for field in [
        'smiles', 'formula', 'commonName', 'mol2D'
    ])


def test_get_details_batch():
    """Test get_extended_compound_info_list returns info for a list of record IDs."""
    info = cs.get_details_batch([6543, 1235, 6084])
    assert len(info) == 3
    assert all(field in info[0] for field in [
        'id', 'smiles', 'formula', 'averageMass', 'molecularWeight', 'monoisotopicMass', 'nominalMass',
        'commonName', 'referenceCount', 'dataSourceCount', 'pubMedCount', 'rscCount', 'mol2D'
    ])
    assert all(isinstance(info[0][field], float) for field in [
        'averageMass', 'molecularWeight', 'monoisotopicMass'
    ])
    assert isinstance(info[0]['id'], int)
    assert all(isinstance(info[0][field], six.text_type) for field in [
        'smiles', 'formula', 'commonName', 'mol2D'
    ])


def test_get_external_references():
    """Test get_external_references returns references for a record ID."""
    refs = cs.get_external_references(125)
    assert len(refs) > 5
    for ref in refs:
        assert 'source' in ref
        assert 'sourceUrl' in ref
        assert 'externalId' in ref
        assert 'externalUrl' in ref


def test_get_image():
    """Test get_image returns image data for a record ID."""
    img = cs.get_image(123)
    assert img[:8] == b'\x89PNG\x0d\x0a\x1a\x0a'  # PNG magic number


def test_get_mol():
    """Test get_mol returns a MOLfile for a record ID."""
    mol = cs.get_mol(6084)
    assert 'V2000' in mol
    assert 'M  END' in mol


# Filter

def test_filter_formula_batch():
    """Test filter_formula_batch returns a list of CSIDs."""
    qid = cs.filter_formula_batch(formulas=['C2H2', 'C3H6'])
    while True:
        status = cs.filter_formula_batch_status(qid)
        if status['status'] in {'Suspended', 'Failed', 'Not Found', 'Complete'}:
            break
        time.sleep(1)
    results = cs.filter_formula_batch_results(qid)
    assert len(results) == 2
    for result in results:
        assert 'formula' in result
        assert 'results' in result
        assert len(result['results']) > 1


def test_filter_intrinsicproperty_formula():
    """Test filter_intrinsicproperty returns a list of CSIDs."""
    qid = cs.filter_intrinsicproperty(formula='C6H6')
    while True:
        status = cs.filter_status(qid)
        if status['status'] in {'Suspended', 'Failed', 'Not Found', 'Complete'}:
            break
        time.sleep(1)
    results = cs.filter_results(qid)
    assert len(results) > 10


def test_filter_intrinsicproperty_mass():
    """Test filter_intrinsicproperty returns a list of CSIDs."""
    qid = cs.filter_intrinsicproperty(monoisotopic_mass=500, monoisotopic_mass_range=0.001)
    while True:
        status = cs.filter_status(qid)
        if status['status'] in {'Suspended', 'Failed', 'Not Found', 'Complete'}:
            break
        time.sleep(1)
    results = cs.filter_results(qid)
    assert len(results) > 10


def test_filter_mass():
    """Test filter_mass returns a list of CSIDs."""
    qid = cs.filter_mass(500, 0.001)
    while True:
        status = cs.filter_status(qid)
        if status['status'] in {'Suspended', 'Failed', 'Not Found', 'Complete'}:
            break
        time.sleep(1)
    results = cs.filter_results(qid)
    assert len(results) > 10


def test_filter_mass_batch():
    """Test filter_mass_batch returns a list of CSIDs."""
    qid = cs.filter_mass_batch(masses=[(12, 0.001), (24, 0.001)])
    while True:
        status = cs.filter_mass_batch_status(qid)
        if status['status'] in {'Suspended', 'Failed', 'Not Found', 'Complete'}:
            break
        time.sleep(1)
    results = cs.filter_mass_batch_results(qid)
    print(results)
    assert len(results) == 2
    for result in results:
        assert 'mass' in result
        assert 'range' in result
        assert 'results' in result
        assert len(result['results']) > 0


def test_filter_smiles():
    """Test filter_smiles returns a list of CSIDs."""
    qid = cs.filter_smiles('c1ccccc1')
    while True:
        status = cs.filter_status(qid)
        if status['status'] in {'Suspended', 'Failed', 'Not Found', 'Complete'}:
            break
        time.sleep(1)
    results = cs.filter_results(qid)
    assert len(results) == 1
    assert results[0] == 236  # Benzene ChemSpider ID


def test_filter_sdf():
    """Test filter_results_sdf returns an SDF file."""
    qid = cs.filter_formula('C10H20')
    while True:
        status = cs.filter_status(qid)
        if status['status'] in {'Suspended', 'Failed', 'Not Found', 'Complete'}:
            break
        time.sleep(1)
    sdf = cs.filter_results_sdf(qid)
    assert b'V2000' in sdf
    assert b'$$$$' in sdf


# Tools

def test_convert():
    """Test convert."""
    assert cs.convert('c1ccccc1', 'SMILES', 'InChI') == 'InChI=1S/C6H6/c1-2-4-6-5-3-1/h1-6H'
    assert cs.convert('InChI=1S/C6H6/c1-2-4-6-5-3-1/h1-6H', 'InChI', 'InChIKey') == 'UHOVQNZJYSORNB-UHFFFAOYSA-N'
    assert cs.convert('UHOVQNZJYSORNB-UHFFFAOYSA-N', 'InChIKey', 'InChI') == 'InChI=1S/C6H6/c1-2-4-6-5-3-1/h1-6H'


def test_validate_inchikey():
    """Test validate_inchikey."""
    assert cs.validate_inchikey('UHOVQNZJYSORNB-UHFFFAOYSA-N') is True
    assert cs.validate_inchikey('UHOVQNZJYSORNB-UHFFFAOYSQ-N') is False
    assert cs.validate_inchikey('UHOVQNZJYSORNB-UHFFFAOYSA') is False


# MassSpecAPI

def test_get_databases():
    """Test get_databases returns the list of ChemSpider data sources."""
    with pytest.deprecated_call():
        dbs = cs.get_databases()
        assert all(source in dbs for source in ['Wikipedia', 'ZINC', 'PubChem'])


def test_get_extended_compound_info():
    """Test get_extended_compound_info returns info for a CSID."""
    with pytest.deprecated_call():
        info = cs.get_extended_compound_info(6543)
        assert all(field in info for field in [
            'id', 'smiles', 'formula', 'averageMass', 'molecularWeight', 'monoisotopicMass', 'nominalMass',
            'commonName', 'referenceCount', 'dataSourceCount', 'pubMedCount', 'rscCount', 'mol2D'
        ])
        assert all(isinstance(info[field], float) for field in [
            'averageMass', 'molecularWeight', 'monoisotopicMass'
        ])
        assert isinstance(info['id'], int)
        assert all(isinstance(info[field], six.text_type) for field in [
            'smiles', 'formula', 'commonName', 'mol2D'
        ])


def test_get_extended_compound_info_list():
    """Test get_extended_compound_info_list returns info for a list of CSIDs."""
    with pytest.deprecated_call():
        info = cs.get_extended_compound_info_list([6543, 1235, 6084])
        assert len(info) == 3
        assert all(field in info[0] for field in [
            'id', 'smiles', 'formula', 'averageMass', 'molecularWeight', 'monoisotopicMass', 'nominalMass',
            'commonName', 'referenceCount', 'dataSourceCount', 'pubMedCount', 'rscCount', 'mol2D'
        ])
        assert all(isinstance(info[0][field], float) for field in [
            'averageMass', 'molecularWeight', 'monoisotopicMass'
        ])
        assert isinstance(info[0]['id'], int)
        assert all(isinstance(info[0][field], six.text_type) for field in [
            'smiles', 'formula', 'commonName', 'mol2D'
        ])


def test_get_extended_mol_compound_info_list():
    """Test get_extended_mol_compound_info_list returns info for a list of CSIDs."""
    with pytest.deprecated_call():
        info = cs.get_extended_mol_compound_info_list([1236], include_external_references=True,
                                                      include_reference_counts=True)
        assert len(info) == 1
        assert all(field in info[0] for field in [
            'id', 'smiles', 'formula', 'averageMass', 'molecularWeight', 'monoisotopicMass', 'nominalMass',
            'commonName', 'referenceCount', 'dataSourceCount', 'pubMedCount', 'rscCount', 'mol2D'
        ])
        assert all(isinstance(info[0][field], float) for field in [
            'averageMass', 'molecularWeight', 'monoisotopicMass'
        ])
        assert all(isinstance(info[0][field], int) for field in [
            'id', 'referenceCount', 'dataSourceCount', 'pubMedCount', 'rscCount'
        ])
        assert all(isinstance(info[0][field], six.text_type) for field in [
            'smiles', 'formula', 'commonName', 'mol2D'
        ])


def test_get_record_mol():
    """Test get_record_mol returns a MOL file."""
    with pytest.deprecated_call():
        mol = cs.get_record_mol(6084)
        assert 'V2000' in mol
        assert 'M  END' in mol


# Search

def test_async_simple_search():
    """Test async_simple_search returns a transaction ID."""
    with pytest.deprecated_call():
        rid = cs.async_simple_search('benzene')
        assert re.compile(r'[a-f0-9\-]{20,50}').search(rid)


def test_async_simple_search_ordered():
    """Test async_simple_search returns a transaction ID."""
    with pytest.deprecated_call():
        rid = cs.async_simple_search_ordered('glucose')
        assert re.compile(r'[a-f0-9\-]{20,50}').search(rid)


def test_get_async_search_status():
    """Test get_async_search_status returns the status for a transaction ID."""
    with pytest.deprecated_call():
        rid = cs.async_simple_search('benzene')
        status = cs.get_async_search_status(rid)
        assert status in {
            'Complete', 'Suspended', 'Failed', 'Not Found', 'Unknown', 'Created', 'Scheduled', 'Processing',
            'Suspended', 'PartialResultReady', 'ResultReady'
        }


def test_get_async_search_status_and_count():
    """Test get_async_search_status_and_count returns the status for a transaction ID."""
    with pytest.deprecated_call():
        rid = cs.async_simple_search('benzene')
        while True:
            status = cs.get_async_search_status_and_count(rid)
            if status['status'] in {'Created', 'Scheduled', 'Processing'}:
                continue
            assert status['count'] == 1
            assert status['message'] == 'Found by approved synonym'
            break


def test_get_async_search_result():
    """Test get_async_search_result returns a list of CSIDs."""
    with pytest.deprecated_call():
        rid = cs.async_simple_search('benzene')
        while True:
            status = cs.get_async_search_status(rid)
            if status in {'Created', 'Scheduled', 'Processing'}:
                continue
            assert [c.csid for c in cs.get_async_search_result(rid)] == [236]
            break


def test_get_async_search_result_part():
    """Test get_async_search_result_part returns a list of CSIDs."""
    with pytest.deprecated_call():
        rid = cs.async_simple_search('glucose')
        while True:
            status = cs.get_async_search_status(rid)
            if status in {'Created', 'Scheduled', 'Processing'}:
                continue
            assert len(cs.get_async_search_result_part(rid)) > 6
            assert len(cs.get_async_search_result_part(rid, start=2)) > 2
            assert len(cs.get_async_search_result_part(rid, start=2, count=2)) == 2
            assert len(cs.get_async_search_result_part(rid, start=2, count=99)) > 2
            break


def test_get_compound_info():
    """Test get_compound_info returns info for a CSID."""
    with pytest.deprecated_call():
        info = cs.get_compound_info(123)
        assert all(field in info for field in ['id', 'smiles'])
        assert isinstance(info['id'], int)
        assert isinstance(info['smiles'], six.text_type)


def test_get_compound_thumbnail():
    """Test get_compound_thumbnail returns image data for a CSID."""
    with pytest.deprecated_call():
        img = cs.get_compound_thumbnail(123)
        assert img[:8] == b'\x89PNG\x0d\x0a\x1a\x0a'  # PNG magic number


def test_simple_search():
    """Test simple_search returns a list of CSIDs."""
    assert all(csid in [c.csid for c in cs.simple_search('glucose')] for csid in [5589, 58238, 71358, 96749, 9312824, 9484839])


# Errors


def test_invalid_api_key():
    """Test ChemSpiPyAuthError is raised if a token with invalid format is used."""
    with pytest.raises(errors.ChemSpiPyAuthError):
        mf = ChemSpider('abcde1-1346fa-934a').get_compound(2157).molecular_formula


def test_invalid_api_key2():
    """Test ChemSpiPyAuthError is raised if a fake token with correct format is used."""
    with pytest.raises(errors.ChemSpiPyAuthError):
        mf = ChemSpider('6qBA6lrJycPAYTTcajkkaN02brz5S6Ee').get_compound(2157).molecular_formula


def test_invalid_query_id():
    """Test ChemSpiPyBadRequestError is raised when an invalid query ID is used."""
    with pytest.raises(errors.ChemSpiPyBadRequestError):
        cs.filter_status('xxxxxx')


def test_expired_query_id():
    """Test ChemSpiPyBadRequestError is raised when a valid but expired query ID is used."""
    with pytest.raises(errors.ChemSpiPyBadRequestError):
        cs.filter_status('1a93ee87-acbe-4caa-bc3b-23c3ff39be0f')


def test_fictional_query_id():
    """Test ChemSpiPyBadRequestError is raised when a valid but made up query ID is used."""
    with pytest.raises(errors.ChemSpiPyBadRequestError):
        cs.filter_status('1a93ee87-acbe-4caa-bc3b-23c3ff39be0a')
