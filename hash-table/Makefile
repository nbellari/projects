all:  main.o hash_table.o
	gcc -o a.out main.o hash_table.o -lm

main.o: main.c
	gcc -g -c main.c -o main.o

hash_table.o: hash_table.c
	gcc -g -c hash_table.c -o hash_table.o

clean:
	rm -f *.o a.out
