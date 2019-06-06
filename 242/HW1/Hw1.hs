module Hw1 where

type Mapping = [(String, String, String)]
data AST = EmptyAST | ASTNode String AST AST deriving (Show, Read)

writeExpression :: (AST, Mapping) -> String
evaluateAST :: (AST, Mapping) -> (AST, String)
-- DO NOT MODIFY OR DELETE THE LINES ABOVE -- 
-- IMPLEMENT writeExpression and evaluateAST FUNCTION ACCORDING TO GIVEN SIGNATURES -- 

--import Data.Char(digitToInt)

reader :: AST -> String
reader EmptyAST = ""
reader (ASTNode str EmptyAST EmptyAST) =str 
reader (ASTNode "num" left EmptyAST) = reader left
reader (ASTNode "str" left EmptyAST) = readerHelp left
reader (ASTNode "negate" left EmptyAST) = "(-" ++ reader left ++")"
reader (ASTNode "len" left EmptyAST) = "(length " ++ reader left ++ ")"
reader (ASTNode str left right) = "("++ (reader left) ++( strReader str) ++ (reader right) ++")"

readerHelp :: AST -> String
readerHelp (ASTNode str EmptyAST EmptyAST) = "\"" ++ str ++ "\""

strReader:: String -> String
strReader "plus" = "+"
strReader "times" = "*"
strReader "cat" = "++"
strReader x = x

mapperReader :: Mapping -> String
mapperReader [] = ""
mapperReader [x] = mapperWriter x
mapperReader (x:xs) =  mapperWriter x ++ ";" ++ mapperReader xs

mapperWriter :: (String, String, String) -> String
mapperWriter (a,"str",c) = a++ "=\"" ++ c++ "\""
mapperWriter (a,"num",c) = a++ "=" ++ c


writeExpression (x,[]) = reader x 
writeExpression (x, y) = "let " ++ mapperReader y ++ " in " ++ reader x 

--------------- upper is all write -------------

--evaluateAST :: (AST, Mapping) -> (AST, String)
evaluateAST (x,y) = do let t = astCorrector (x,y) in (t, astShorter t)

intToChar :: Int -> String
intToChar x = do let t = show x :: String in t

stringToInt :: String -> Int
stringToInt x = do let t = read x :: Int in t 

--(ASTNode "num" (ASTNode "3" EmptyAST EmptyAST) EmptyAST),"3")
--

astShorter :: AST -> String
astShorter (ASTNode "num" (ASTNode a EmptyAST EmptyAST) EmptyAST) = a 
astShorter (ASTNode "str" (ASTNode a EmptyAST EmptyAST) EmptyAST) = a 
astShorter (ASTNode "plus" left right ) = intToChar( stringToInt(astShorter left) + stringToInt(astShorter right))
astShorter (ASTNode "times" left right) =  intToChar( stringToInt(astShorter left) * stringToInt(astShorter right))
astShorter (ASTNode "negate" left EmptyAST) =  intToChar( stringToInt(astShorter left) * (-1 ))
astShorter (ASTNode "cat" left right) = astShorter left  ++ astShorter right
astShorter (ASTNode "len" left EmptyAST) =  intToChar(length( astShorter left))



astCorrector :: (AST, Mapping)->  AST
astCorrector (x,[]) = x
astCorrector (x ,[a]) = correctHelp x a 
astCorrector (x ,(a:as)) = astCorrector ((correctHelp x a) ,as)


correctHelp :: AST -> (String,String,String) -> AST
correctHelp (ASTNode t EmptyAST EmptyAST) (y, "num", c) = if t == y  then ASTNode "num" (ASTNode c EmptyAST EmptyAST) EmptyAST else (ASTNode t EmptyAST EmptyAST)
correctHelp (ASTNode t EmptyAST EmptyAST) (y, "str", c) = if t == y  then ASTNode "str" (ASTNode c EmptyAST EmptyAST) EmptyAST else (ASTNode t EmptyAST EmptyAST)
correctHelp (ASTNode "num" left EmptyAST) a = ASTNode "num" left EmptyAST
correctHelp (ASTNode "str" left EmptyAST) a = ASTNode "str" left EmptyAST
correctHelp (ASTNode str left EmptyAST) a = ASTNode str (correctHelp left a) EmptyAST
correctHelp (ASTNode str left right) a = ASTNode str (correctHelp left a) (correctHelp right a) 

isNumber :: String -> Bool
isNumber (x:xs) = if isMember x ['0','1','2','3','4','5','6','7','8','9','-'] then isNumber xs else False
isNumber [] = True
 
isMember n [] = False
isMember n (x:xs)
    | n == x = True
    | otherwise = isMember n xs