module Hw2 where

data ASTResult = ASTError String | ASTJust (String, String, Int) deriving (Show, Read)
data ASTDatum = ASTSimpleDatum String | ASTLetDatum String deriving (Show, Read)
data AST = EmptyAST | ASTNode ASTDatum AST AST deriving (Show, Read)

isNumber :: String -> Bool
eagerEvaluation :: AST -> ASTResult
normalEvaluation :: AST -> ASTResult
-- DO NOT MODIFY OR DELETE THE LINES ABOVE -- 
-- IMPLEMENT isNumber, eagerEvaluation and normalEvaluation FUNCTIONS ACCORDING TO GIVEN SIGNATURES -- 

isNumber(x:xs) = if x=='-' then isNumberx xs else isNumberx(x:xs)
isNumber []= False


isNumberx (x:xs) = if isMember x ['0','1','2','3','4','5','6','7','8','9'] then isNumberx xs else False
isNumberx [] = True
 
isMember n [] = False
isMember n (x:xs) = if n == x  then True else isMember n xs

strNum :: String
strNum = "num"

strStr :: String
strStr = "str"


normalEvaluation (ASTNode (ASTLetDatum t)  lol (ASTNode (ASTLetDatum x)  left right)) = 
    let newast = normalCorrector(right,x,left)
        cou = counter newast
        son = astShorter(newast)
    in if fst' son == False then ASTError (snd' son) else if "num" == trd son then ASTJust (snd' son,"num",cou) else ASTJust (snd' son,"str",cou) 
normalEvaluation (ASTNode (ASTLetDatum x)  left right) = 
    let newast = normalCorrector(right,x,left)
        cou = counter newast
        son = astShorter(newast)
    in if fst' son == False then ASTError (snd' son) else if "num" == trd son then ASTJust (snd' son,"num",cou) else ASTJust (snd' son,"str",cou) 
normalEvaluation a = 
    let son = astShorter a
        cou = counter a
    in if fst' son == False then ASTError (snd' son) else if "num" == trd son then ASTJust (snd' son,"num",cou) else ASTJust (snd' son,"str",cou) 

	
	
eagerEvaluation  (ASTNode (ASTLetDatum t)  lol (ASTNode (ASTLetDatum x)  left right)) = 
    let lefty = astShorter left
        sonuc = snd' lefty
        righty = astShorter(eagerCorrector(right,x, sonuc))
        maga = (snd' righty)
        cou = counter left + counter right + counter lol
    in  if fst' lefty == False then ASTError (snd' lefty) else if fst' righty == False then ASTError (snd' righty) else if "num" == trd righty then ASTJust(maga , "num" ,cou) else ASTJust(maga , "str" ,cou)
eagerEvaluation  (ASTNode (ASTLetDatum x)  left right) = 
    let lefty = astShorter left
        sonuc = snd' lefty
        righty = astShorter(eagerCorrector(right,x, sonuc))
        maga = (snd' righty)
        cou = counter left + counter right
    in  if fst' lefty == False then ASTError (snd' lefty) else if fst' righty == False then ASTError (snd' righty) else if "num" == trd righty then ASTJust(maga , "num" ,cou) else ASTJust(maga , "str" ,cou)
eagerEvaluation a = 
    let lefty = astShorter a
        cou = counter a
    in  if fst' lefty == False then ASTError (snd' lefty)  else if "num" == trd lefty then ASTJust(snd' lefty , "num",cou) else ASTJust(snd' lefty , "str" ,cou)


fst' (x,y,z) = x
snd' (x,y,z) = y
trd (x,y,a) = a
		
intToChar :: Int -> String
intToChar x = do let t = show x :: String in t

stringToInt :: String -> Int
stringToInt x = do let t = read x :: Int in t 

eagerCorrector :: (AST,String,String) -> AST 
eagerCorrector ((ASTNode (ASTSimpleDatum torep) EmptyAST EmptyAST),x,sonuc) = if x == torep then if isNumber sonuc then (ASTNode (ASTSimpleDatum "num") (ASTNode (ASTSimpleDatum sonuc) EmptyAST EmptyAST) EmptyAST) else (ASTNode (ASTSimpleDatum "str") (ASTNode (ASTSimpleDatum sonuc) EmptyAST EmptyAST) EmptyAST) else ASTNode (ASTSimpleDatum torep) EmptyAST EmptyAST 
eagerCorrector ((ASTNode (ASTSimpleDatum x)  left right),  a, sonuc) = ASTNode (ASTSimpleDatum x)  (eagerCorrector (left,a,sonuc)) (eagerCorrector (right,a,sonuc))

normalCorrector :: (AST,String,AST) -> AST
normalCorrector ((ASTNode (ASTSimpleDatum torep) EmptyAST EmptyAST),x,sonuc) = if x == torep then sonuc  else (ASTNode (ASTSimpleDatum torep) EmptyAST EmptyAST)
normalCorrector ((ASTNode (ASTSimpleDatum x)  left right),  a, sonuc) = ASTNode (ASTSimpleDatum x)  (normalCorrector (left,a,sonuc)) (normalCorrector (right,a,sonuc))
--normalCorrector (EmptyAST,a,sonuc) = EmptyAST


counter :: AST -> Int
counter (ASTNode (ASTSimpleDatum "plus") left right )= counter left +1+ counter right
counter (ASTNode (ASTSimpleDatum "negate") left right )= counter left +1+ counter right
counter (ASTNode (ASTSimpleDatum "times") left right )= counter left +1+ counter right
counter (ASTNode (ASTSimpleDatum "cat") left right )= counter left +1+ counter right
counter (ASTNode (ASTSimpleDatum "len") left right )= counter left +1+ counter right
counter x = 0



astShorter :: AST  -> (Bool,String,String)
astShorter (ASTNode (ASTSimpleDatum "num") (ASTNode (ASTSimpleDatum a) EmptyAST EmptyAST) EmptyAST)  = if isNumber a then (True,a,"num") else (False,"the value '" ++ a++"' is not a number!","")
astShorter (ASTNode (ASTSimpleDatum "str") (ASTNode (ASTSimpleDatum a) EmptyAST EmptyAST) EmptyAST)  = (True,a,"str") 
astShorter (ASTNode (ASTSimpleDatum "plus") left right ) =
    let a = astShorter left 
        b = astShorter right 
    in  if fst' a == False then a else if fst' b == False then b else if (("num" == trd a) && ("num" == trd b)) then (True, intToChar( stringToInt(snd' a) + stringToInt(snd' b)),"num") else  (False,"plus operation is not defined between "++ trd a ++ " and " ++ trd b ++ "!","")
astShorter (ASTNode (ASTSimpleDatum "times") left right) =
    let a = astShorter left 
        b = astShorter right 
    in  if fst' a == False then a else if fst' b == False then b else if (("num" == trd a) && ("num" == trd b)) then (True, intToChar( stringToInt(snd' a) * stringToInt(snd' b)),"num") else  (False,"times operation is not defined between "++ trd a ++ " and " ++ trd b ++ "!","")
astShorter (ASTNode (ASTSimpleDatum "negate") left EmptyAST) =  let a = astShorter left in if fst' a == False then a else if trd a == "num" then 	(True, intToChar( stringToInt(snd' a) * (-1 )), "num") else (False,"negate operation is not defined on str!","")
astShorter (ASTNode (ASTSimpleDatum  "cat" ) left right) =
    let a = astShorter left 
        b = astShorter right 
    in  if fst' a == False then a else if fst' b == False then b else if (("str" == trd a) && ("str" == trd b)) then (True, snd' a ++ snd' b,"str") else  (False,"cat operation is not defined between "++ trd a ++ " and " ++ trd b ++ "!","") 
astShorter (ASTNode (ASTSimpleDatum "len" )  left EmptyAST) =  let a = astShorter left in if fst' a == False then a else if trd a == "str" then (True,intToChar(length( snd' a)),"num") else (False,"len operation is not defined on num!","")
--astShorter x = (False, "son","case")