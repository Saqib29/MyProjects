#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

char board[3][3] = {{'1', '2', '3'}, {'4', '5', '6'}, {'7', '8', '9'}};
char current_marker;
int current_player;

void drawBoard()
{
    cout << "\n\n";
    cout << "     " << board[0][0] << " | " << board[0][1] << " | " << board[0][2] << endl;
    cout << "    ----------- \n";
    cout << "     " << board[1][0] << " | " << board[1][1] << " | " << board[1][2] << endl;
    cout << "    ----------- \n";
    cout << "     " << board[2][0] << " | " << board[2][1] << " | " << board[2][2] << endl;
    cout << "\n\n";
}
bool placeMaker(int slot)
{
    int row = slot/3;
    int col;

    (slot%3  == 0) ? row -= 1, col = 2 : col = (slot%3)-1;

    if(board[row][col] != 'x' && board[row][col] != 'o'){
        board[row][col] = current_marker;
        return true;
    }
    else return false;
}
int winner()
{
   for(int i=0; i<3; i++)
   {
       if(board[i][0] == board[i][1] && board[i][1] == board[i][2]) return current_player;
       if(board[0][i] == board[1][i] && board[1][i] == board[2][i]) return current_player;
   }
   if(board[0][0] == board[1][1] && board[1][1] == board[2][2]) return current_player;
   if(board[0][2] == board[1][1] && board[1][1] == board[2][0]) return current_player;

   return 0;
}
void swap__player_amd_marker()
{
    (current_marker == 'x') ? current_marker = 'o' : current_marker = 'x';

    (current_player == 1) ? current_player = 2 : current_player = 1;
}
void game()
{
    cout << "Player one, choose your marker: ";
    char marker_p1;
    cin >> marker_p1;

    current_player = 1;
    current_marker = marker_p1;

    drawBoard();
    int player_won;

    for(int i=0; i<9; i++)
    {
        cout << "It's player " << current_player << "'s turn. Enter your slot: ";
        int slot;
        cin >> slot;
        if(slot < 1 || slot > 9){
            cout << "That slot is invalid! try another slot\n";
            i--;
            continue;
        }
        if(!placeMaker(slot)){
            cout << "This slot is already occupied, try another\n";
            i--;
            continue;
        }
        drawBoard();

        player_won = winner();

        if(player_won == 1) {
            cout << "Player one won! congratulations!\n";
            break;
        }
        if(player_won == 2){
            cout << "Player two won! congratulations!\n";
            break;
        }

        swap__player_amd_marker();

    }
    if(player_won == 0)
        cout << "This is a tie game!";
}

int main()
{
    game();

    return 0;
}
