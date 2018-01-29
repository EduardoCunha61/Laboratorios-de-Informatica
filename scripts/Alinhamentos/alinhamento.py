# -*-coding: utf-8 -*-

from Bio import Phylo


print("\n", "Locus_tag: 'lpg0936'", "\n")
tree = Phylo.read("prot1_phylotree.newick", "newick")
print(tree, "\n")

Phylo.draw_ascii(tree)


print("\n", "Locus_tag: 'lpg1177'", "\n")
tree2 = Phylo.read("prot2_phylotree.newick", "newick")
print(tree2, "\n")

Phylo.draw_ascii(tree2)


print("\n", "Locus_tag: 'lpg1178'", "\n")
tree3 = Phylo.read("prot3_phylotree.newick", "newick")
print(tree3, "\n")

Phylo.draw_ascii(tree3)


print("\n", "Locus_tag: 'lpg1179'", "\n")
tree4 = Phylo.read("prot4_phylotree.newick", "newick")
print(tree4, "\n")

Phylo.draw_ascii(tree4)


print("\n", "Locus_tag: 'lpg1180'", "\n")
tree5 = Phylo.read("prot5_phylotree.newick", "newick")
print (tree5, "\n")

Phylo.draw_ascii(tree5)


