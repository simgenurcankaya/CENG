#include<stdio.h> 
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(char argc,char* argv[]){
	int p1,p2;
	//int i =0;
	int fd[2][2];
	FILE * fp =  fopen("out.txt", "w" );
	int  buffer_size = 1024;
	char * buffer = (char*) malloc(buffer_size);
	pipe(fd[0]);
	pipe(fd[1]);
	int i = 0, j =0 ;
	if (p1=fork()) { //parent 
	
		if(p2 = fork()){ // parent
			int c;
			close(fd[0][0]); // close read pipe
			close(fd[1][0]);
			while(fgets(buffer,buffer_size, stdin)!=NULL){
				if(i%2 == 0){
					dup2(fd[0][1],1);
					write(1,buffer, buffer_size); 
				} 
				
				else{
					dup2(fd[1][1],1);
					write(1,buffer, buffer_size);
				} 
				i++;
			}
			close(fd[0][1]);
			close(fd[1][1]);	
			wait(&c); // bekliyo bayaa uzun
			wait(&c); 
			close(1);  // output yok,

		} 
		
		else {  //child 1
		char * yedek = (char*) malloc(buffer_size);
		char * sim = (char*) malloc(buffer_size);
		close(fd[0][1]); // pipe write ı kapat
		close(fd[1][1]);
		dup2(fd[0][0],0); 
		close(fd[0][0]); // pipe ı kapat
		close(fd[1][0]);
		while (i<4) {
			read(0,sim,1024);
			printf("read1: %s",sim);
			i++;
			}
		close(0);

		}
	}
	else {  //child 2
		char * yedek = (char*) malloc(buffer_size);
		char * sim = (char*) malloc(buffer_size);
		close(fd[0][1]); // pipe write ı kapat
		close(fd[1][1]);
		dup2(fd[1][0],0);
		close(fd[0][0]); // pipe ı kapat
		close(fd[1][0]); 
		while (j<4) {
			read(0,sim,1024);
			printf("read2: %s",sim);
			j++;
			}
		close(0);

		}

	return 0; 
} 
