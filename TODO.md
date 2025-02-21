1. Make a lightwieght web-app (locally) using fastapi that can process these requests:  
-get request to see list of problems  
-get request to see a particular problem by id  
-post request with code of a program to solve a particular problem (always returns 200 at this point)  
(at this point problems are just txt/json files with problem statement and testcases)  
2. Build upon it. Actually process the code.  
3. Buid upon it with some AI features - call to LLM API (like DeepSeek)  
-rate solution based on namings, practices and such  
-(optional, maybe later) generate a problem about particular topic  
-(optional, maybe later) check solution for correctness (for previous case, when I do not have testcases)  
-(optional, maybe later) provide AI with both custom problem and solution and get verdict  
4. Make a database so problems, testcases, etc. would be there instead of just files. Handle to add problems easily (with admin rights only)  
4.5. Make users (meaning registration and authentication) as entities in the db  
5. Frontend?  
6. Either use service like judge0 or write safe mechanisms to process the code myself  
7. Add support for different languages?  
8. Deploy?  