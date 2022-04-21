from dask import delayed

def parallel_estimate_pi(nsamples):
    points = [delayed(is_inside_circle)() for _ in range(nsamples)]
    return 4. * delayed(sum)(points) / nsamples

print(parallel_estimate_pi(10000).compute())
