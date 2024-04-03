#include <iostream>
#include <vector>
#include <fstream>
#include <cstdlib>
#include <thread>
#include <chrono>
#include <random>
#include <string>

using namespace std;

void gameOfLife(vector<vector<int>> & board) {
        
	int n = board[0].size();
	int m = board.size();
	int count;

	vector<vector<int>> copyBoard = board;

	vector<vector<int>> dirs{{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};

	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {

			count = 0;

			for (auto & dir : dirs) {
				int x = i + dir[0], y = j + dir[1];
				if (x < 0 || y < 0 || x >= m || y >= n) continue;
				count += copyBoard[x][y]; 
			}

			if (copyBoard[i][j] && (count < 2 || count > 3)) board[i][j] = 0;
			else if (!copyBoard[i][j] && count == 3) board[i][j] = 1;

		}
	}

}

void readBoard(const string & fileName, vector<vector<int>> & board) {

	ifstream in(fileName);
	string line;

	while (getline(in, line)) {
		vector<int> row;
		for (char c : line) {
			row.push_back(c - '0');
		}
		board.push_back(row);
	}

}

void printBoard(vector<vector<int>> & board) {

	int m = board[0].size();
	int n = board.size();

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cout << (board[i][j] ? "█" : " ");
		}
		cout << endl;
	}

	this_thread::sleep_for(chrono::milliseconds(150));

}

void cleanScreen() { 
	
	#ifdef _WIN32
		std::system("cls");
	#else
		std::system("clear");
	#endif

}

void generatePattern(const string & filename, int width, int height) {
	
	random_device rd;
	mt19937 gen(rd());
	discrete_distribution<> d({50, 50});

	ofstream out(filename);

	for (int i = 0; i < height; ++i) {
		for (int j = 0; j < width; ++j) {
			out << d(gen);
		}
		out << '\n';
	}

}

int main() {

	generatePattern("test.txt", 350, 100);

	vector<vector<int>> board;

	readBoard("test.txt", board);

	while (1) {
		cleanScreen();
		printBoard(board);
		gameOfLife(board);
	}

	return 0;

}
