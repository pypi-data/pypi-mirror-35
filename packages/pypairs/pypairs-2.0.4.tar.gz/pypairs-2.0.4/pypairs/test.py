from pypairs import wrapper

t = wrapper.sandbag_from_file("/Users/rfechtner/Desktop/ICMData/TrainingDataCombined/training_matrix.csv", "/Users/rfechtner/Desktop/ICMData/TrainingData1/cellAnnotation-sub.tsv", sep_annotation="\t", filter_genes_dispersion=True, processes=7, fraction=0.7, rm_zeros=True, random_subset=5)