#include<stdio.h> 
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <string.h>
int main(char argc,char* argv[]){
	int p1 = getpid();
	int n = atoi(argv[1]);
	int fd[n][2];
	int  buffer_size = 1023;
	char  buffer[1023] ;
	char suh[100]= "./";
	strcat(suh , argv[2]);
	//printf("suh:: %s %d\n",suh,argc);
	if(argc == 3){
	for(int i = 0 ; i<n ; i++){
		pipe(fd[i]);
	}
	int aq = 0;
	int i = 0;
	int a = 0;
	
	while(fgets(buffer,buffer_size, stdin)){
		//printf("HALO %s \n", buffer);
		//fflush(stdout);
		write(fd[i%n][1],buffer, strlen(buffer));  
		i++;
	}
	i = 0;
	while(i<n){
		
		if(p1 == getpid()){ // parentsa
			if(fork() == 0){ //child
				close(fd[i][1]);
				dup2(fd[i][0],0); 
				close(fd[i][0]);
				aq = i;

				
			}
			else{ // parent
				close(fd[i][0]); //childları kapıyo
				close(fd[i][1]); //childları kapıyo
				close(0);
				
			}   
		}
		i++;
	}
	
	char simg[100];
	sprintf(simg, "%d", aq);
	if(p1 != getpid()){
		execl(suh, suh, simg , NULL);
	}
	
	}
	return 0;
	
}
