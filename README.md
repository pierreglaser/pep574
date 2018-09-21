Benchmark repository that traces the peaktime memory usage of numpy array pickling

# Requirements

* Antoine Pitrou's [python3.8 branch](https://github.com/pitrou/cpython/tree/pickle5)
* My [numpy's branch](https://github.com/pierreglaser/numpy/tree/implement-reduce-ex)
* [airspeed velocity](https://asv.readthedocs.io/en/stable/)


# Installing

* Follow python instruction to [build python from source](https://docs.python.org/3/using/unix.html)
* Clone my numpy fork, and checkout to the implement-reduce-ex branch
* Clone this repository in the same parent directory than numpy
* Run asv quickstart and follow the instructions
* Run the benchmarks on the my branch's last commit using the commmand `asv run implement-reduce-ex^!` 
