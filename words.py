#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <vector>

using namespace std;

struct TreeNode{
        string word;               //word will store the word from text file
        vector<int>lines;          //for keeping record of lines in which it was found
        TreeNode*left;             //pointer to left subtree
        TreeNode*right;            //pointer to right subtree
        TreeNode*temp;
    }; //end TreeNode

//check function for comparing strings
bool check(string a,string b)
{
    if(a<b)
      return false;
    return true;
}//end check

void insert(TreeNode *root,string word,int lineNumber){
    //Tree is NULL
   if(root==NULL){
      root=new TreeNode();
      root->word=word;
      root->lines.push_back(lineNumber);
   }//end if
    //words match
   if(root->word==word)
      root->lines.push_back(lineNumber);

   //check(a,b)is function that returns 1 if 'string a' is bigger than 'string b' lexographically
   if(check(root->word,word)){ //present word is lexographically bigger than root word
      if(root->right)          //if right node to root is not null we insert word recursively
        insert(root->right,word,lineNumber);
      else{                    //if right node is NULL a new node is created
        TreeNode*temp=root->right;
        temp=new TreeNode();
        temp->word=word;
        temp->lines.push_back(lineNumber);
     }//end else
    }//end if
    else{ //present word is lexographically smaller than root word
      if(root->left)
        insert(root->left,word,lineNumber);
      else{
        TreeNode*temp=root->left;
        temp=new TreeNode();
        temp->word=word;
        temp->lines.push_back(lineNumber);
      }//end nested else
    }//end else
}//end insert

//Print tree in In-Order traversal
void InOrder(TreeNode* node)
{
    if(!node) //end if pointing to null
        return;
    InOrder(node->left);        //display the left subtree
    cout << node->word << " ";  //display current node
    InOrder(node->right);        //display the right subtree
}//end InOrder

int main() { //main
	//int lineNumber = 0; //number of lines
	ifstream file("text.txt"); //takes input stream from designated file
	if(file) { //if file is there
		string line, word ; //setting line and word strings
		while(getline(file, line)) { //getting the lines from the file
            //++lineNumber; //incrementing number of lines when a new line is read
			istringstream is(line); //checking for a line
			while(is >> word) { //while a word exists
				InOrder(root); //<< lineNumber << "\n"; //outputting the words and tabbing to then print the line number and then a new line
			}//end word while
		}//end getline while
	}//end file if
	file.close();
	file.clear();
	return 0;
}//end main
