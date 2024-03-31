# BioComputing
Q. Write a program to model a single nucleotide mutation and to observe changes in the protein sequence after N steps. 

1. Take ORF (prj14.fasta) sequence and translate into protein sequence
(store protein sequence).


2. Now, choose a position at random and replace (mutate) nucleotide at the
position with another nucleotide at random. (self nucleotide change is
allowed).


3. Subsequent to mutation, translate into protein sequence.


4. Repeat steps 2 to 3 for N (N=100) times and find number of amino acid
changes between initial and final sequence after N steps.


Note: If at any step the protein is shorter by 50% than initial protein length,
then restart mutation from N=1. 

If at any step, there is no stop codon then restart mutation step from N=1.

Plot number of amino acid changes with the number of steps.

------------------------------------------------------------------END Question----------------------------------------------------------------------------
Although it is a O(1) complexity problem, [it is a O(n*num_steps) complexity problem, but since n and and Num_steps are fixed it becomes O(1); n= length of sequence], it takes about 7-8 mins to run, There may be better way to code this to decrease time, but since I only know a little bit of coding, I am sticking to howmuch I understood.

I have originally written this code in a JupyterNotebook.

Altough this sheet only contains the final code, full process and progress can be found in this [Colab sheet](https://colab.research.google.com/drive/1zs3112tGsHNnB1fYUqicYc80uHesvAcJ?usp=sharing)

I have coded taking help from the following refrences.

References:


1.   https://www.youtube.com/watch?v=kQyb_6RYkqs
2.   https://www.youtube.com/watch?v=jBlTQjcKuaY
3.   https://www.youtube.com/watch?v=8SLk_uRRcgc
4.   https://www.youtube.com/watch?v=rgeeUv5YylE
5.   https://www.youtube.com/watch?v=5-3DBnJyuPo
6.   https://www.youtube.com/watch?v=_uQrJ0TkZlc
7.   https://www.youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg
8.   https://www.researchgate.net/post/How_to_perform_a_single-point_mutation_in_a_PDB_file_using_Biopython


