from Bio import SeqIO

for record in SeqIO.parse("brca1.fasta", "fasta"):
    print("ID :",record.id)
    print( "SEQUENCE: ",record.seq)
    print("LENGTH: ",len(record.seq))

    print("A: ", record.seq.count("A"))
    print("T: ", record.seq.count("T"))
    print("G: ", record.seq.count("G"))
    print("C: ", record.seq.count("C"))
  
    print("Complement sequence: ", record.seq.complement())

    print("GC content:", ((record.seq.count("G")+record.seq.count("C"))/len(record.seq)*100))

    print("Proteins: ", record.seq.translate())

    if "ATG" in record.seq:
        print("The sequence contains a start codon")
    else:
        print("The sequnece doesn't contain a start codon")
