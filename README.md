# NeuralNetworkBasedBranchPredictor
Branch prediction using simple perceptron and path based perceptron 



To run gem5 and replicate our experiments and results:
  
1. Change into gem5 directory
2. scons build/X86/gem5.opt -j3 (3 if you have 2 cores, on gem5 site it says use the number of cores on your machine + 1)
3. python extract_results.py(This will automatically run all the benchmark programs on all the branch predictors)
4. The results will be in evaluations/X86.


NOTES
The branch predictors are located at src/cpu/pred
Our additions are:
1. perceptron.hh
2. perceptron.cc
3. pathperceptron.hh
4. pathperceptron.cc
