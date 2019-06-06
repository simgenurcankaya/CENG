:− module(hw5,[catomic_number/2 ,ion/2 ,molecule/2]).
:− [catoms].

sum([],T) :- T is 0.
sum([A],T) :- T is A.
sum([A|B],T):- sum(B,Y) -> T is A+Y.
	
last_element([X],T):- X>4 -> T is X-8; T is X.
last_element([_|Tail],T):-last_element(Tail,T).

	
catomic_number(Name,CATOMIC_NUMBER) :-[catoms] , catom(Name,_,_,Electron), sum(Electron,CATOMIC_NUMBER).

ion(Name,CHARGE) :- [catoms],  catom(Name,_,_,Electron), last_element(Electron,CHARGE).

molecule(CATOM_LIST,TOTAL_CATOMIC_NUMBER) :- sum_list(CATOM_LIST,TOTAL_CATOMIC_NUMBER), sum_ion(CATOM_LIST,0),!.
molecule(CATOM_LIST,TOTAL_CATOMIC_NUMBER) :- simg(L), solve(TOTAL_CATOMIC_NUMBER,L,CATOM_LIST).


sum_list([], 0). 
sum_list([X],T) :- catomic_number(X,T),!.
sum_list([X|Y],T) :- sum_list(Y,B), catomic_number(X,Z) -> T is Z+B.

sum_ion([], 0).
sum_ion([X],T) :- ion(X,T),!.
sum_ion([X|Y],T) :- sum_ion(Y,B), ion(X,Z) -> T is Z+B.

nmember(X,[X|_]).
nmember(X,[_|R]) :- nmember(X,R). 

people(L) :- [catoms] , findall(X, catom(X,_,_,_), L).

solve(MaxVal,Lin,Lout):- MaxVal=<150, [catoms], msubset(Lin,Lout,MaxVal,0,8), sum_ion(Lout,0),  sum_list(Lout,MaxVal).
solve(MaxVal,_,_):- MaxVal>150.

simg(T) :- people(L), merge_sort(L,T).

msubset( _, [],_,_,_).
msubset([H|X1], [H|T1],MAX,YET,Bas):- Bas>0, MAX>=YET, catomic_number(H,RN), Y1 is YET+RN, B1 is Bas-1, MAX>=Y1, msubset([H|X1],T1,MAX,Y1,B1).
msubset([_|X1], [H|T1],MAX,YET,Bas):- Bas>0, MAX>=YET, nmember(H,X1), msubset(X1,[H|T1],MAX,YET,Bas).

merge_sort([],[]).     % empty list is already sorted
merge_sort([X],[X]).   % single element list is already sorted
merge_sort(List,Sorted):-
    List=[_,_|_],divide(List,L1,L2),     % list with at least two elements is divided into two parts
	merge_sort(L1,Sorted1),merge_sort(L2,Sorted2),  % then each part is sorted
	merge(Sorted1,Sorted2,Sorted).                  % and sorted parts are merged
merge([],L,L).
merge(L,[],L):-L\=[].
merge([X|T1],[Y|T2],[X|T]):-catomic_number(X,XC), catomic_number(Y,YC), XC=<YC ,merge(T1,[Y|T2],T).
merge([X|T1],[Y|T2],[Y|T]):-catomic_number(X,XC), catomic_number(Y,YC), XC >YC ,merge([X|T1],T2,T).

divide(L,L1,L2):-even_odd(L,L1,L2).	

even_odd(L,E,O):-odd(L,E,O).
   
odd([],[],[]).
odd([H|T],E,[H|O]):-even(T,E,O).
   
even([],[],[]).
even([H|T],[H|E],O):-odd(T,E,O).
				