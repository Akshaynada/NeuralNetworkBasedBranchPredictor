import os
import settings as s

def analyze(isa, executable):
    command = "build/{}/gem5.opt configs/run_configs.py --exec {} --pred {}"
    
    cond_incorrects    = {}
    indirect_incorrect = {}
    for i in range(7):
        os.system(command.format(isa, executable, i))
        name = s.BP_NAMES[i]
        dump = open(s.INPUT_FILE, "r").readlines()

        attributes = {"conditional misses" : "condIncorrect",
                      "indirect misses"    : "branchPredindirectMispredicted",
                      "latency"     : "host_seconds",
		      "sim seconds" : "sim_seconds",
		      "number of conditionals": "condPredicted",
		      "number of indirect lookups": "indirectLookups",
		      "number of instructions": "sim_insts",
                      "number of lookups": "system.cpu.branchPred.lookups",
		      "number of mispredictions": "branchMispredicts"}
	#condPredicted
	#indirectLookups
        attribute_values = [[l.strip() for l in dump
            if attribute in l][0].split()[1] for attribute in attributes.values()]
	
	attribute_mappings = {attribute: [l.strip() for l in dump if attributes[attribute] in l][0].split()[1] for attribute in attributes}
	
        print("===============================================")
        print("Completed {}".format(name))
        print("===============================================")        
        with open("{}/{}/{}_{}.txt".format(s.OUTPUT_DIR, isa,
            name, s.EXEC_NAMES[executable]), "w") as f:
	    
            for attribute, value in zip(attributes, attribute_values):
                f.write("{} : {}\n".format(attribute, value))
	    
	    conditional_misses = float(attribute_mappings["number of mispredictions"])
	    number_of_instructions = float(attribute_mappings["number of instructions"])
	    number_of_conditionals = float(attribute_mappings["number of lookups"])
            f.write("MPKI: {0:.4f}\n".format((conditional_misses / number_of_instructions) * 1000))
	    f.write("Accuracy: {0:.4f}\n".format(1 - conditional_misses/number_of_conditionals))
if __name__ == "__main__":
    for executable in range(len(s.EXEC_NAMES)):
        analyze("X86", executable)
        
