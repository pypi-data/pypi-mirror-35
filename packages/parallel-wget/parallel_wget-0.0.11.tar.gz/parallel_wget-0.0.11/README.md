# Parallel Wget

Fetches URLs in parallel

Example:

```python
import parallel_wget

host='https://data.ngdc.noaa.gov'
path='/instruments/remote-sensing/passive/spectrometers-radiometers/imaging/viirs/dnb_composites/v10/201204/vcmcfg/'

files=['SVDNB_npp_20120401-20120430_00N060E_vcmcfg_v10_c201605121456.tgz']
parallel_wget.parallel_wget(host=host, path=path, files=files)
```

# Development

```
rm -rf build dist
python setup.py sdist
python setup.py bdist_wheel --universal
~/Library/Python/3.6/bin/twine upload dist/*
```

## Troubleshooting

```
export PYTHONPATH=$PYTHONPATH:/Users/aimeebarciauskas/Library/Python/3.6/lib/python/site-packages/
```

## References

[Parallel Processing in Python with AWS Lambda](https://aws.amazon.com/blogs/compute/parallel-processing-in-python-with-aws-lambda/)

# TODO

* Enable override the default host and path in each file object.
* Add option to pass entire URL in files.

