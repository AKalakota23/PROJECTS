/*
Programmer: Akhil Kalakotga
Program: Piano.cpp
Date: 5/29/2022
Version: 1.4
Description: This program will read notes from a file and play the notes on a piano interface
*/


#include <cstdlib>
#include <iostream>
#include <conio.h>
#include <windows.h>
#include <string>
#include <fstream>

using namespace std;

//classes

class Piano {
private:
    string notes;
public: //public 
    char note;
    void DrawPiano(string file);
    void LoadNotes(string filename); // these will be the mutators
    void PlayNotes(); // these will be the accessors
    Piano()
    {
        notes = "";
    }
};


//this function sets cursor position
void gotoxy(int column, int line) {
    COORD coord;
    coord.X = column;
    coord.Y = line;
    SetConsoleCursorPosition(
        GetStdHandle(STD_OUTPUT_HANDLE),
        coord
    );
}
void ShowConsoleCursor(bool showFlag) { //this function hides the consolor cursor
    HANDLE out = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_CURSOR_INFO    cursorInfo;
    GetConsoleCursorInfo(out, &cursorInfo);
    cursorInfo.bVisible = showFlag; // set cursor visibility
    SetConsoleCursorInfo(out, &cursorInfo);
}


void ColorBackground_C4(int color) //sets the color of the background of key c4 
{
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsole, color);

    for (int i = 20; i <= 29; i++)
    {
        for (int j = 3; j <= 48; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 30; i <= 33; i++)
    {
        for (int j = 32; j <= 48; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 22; i <= 31; i++)
    {
        for (int j = 49; j <= 50; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 24; i <= 29; i++)
    {
        for (int j = 51; j <= 51; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }

    /*gotoxy(20, 3);
    cout << "X";
    gotoxy(29, 3);
    cout << "X";
    gotoxy(20, 48);
    cout << "Y";
    gotoxy(29, 48);
    cout << "Y";
    gotoxy(30, 32);
    cout << "Z";
    gotoxy(33, 32);
    cout << "Z";
    gotoxy(30, 48);
    cout << "Z";
    gotoxy(33, 48);
    cout << "Z";
    gotoxy(22, 49);
    cout << "G";
    gotoxy(31, 49);
    cout << "G";
    gotoxy(22, 50);
    cout << "G";
    gotoxy(31, 50);
    cout << "G";
    gotoxy(24, 51);
    cout << "H";
    gotoxy(29, 51);
    cout << "H";*/

}

void ColorBackground_C5(int color) //sets the color of background c5
{
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsole, color);


    for (int i = 140; i <= 149; i++)
    {
        for (int j = 3; j <= 49; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 150; i <= 153; i++)
    {
        for (int j = 32; j <= 49; j++)
        {
            gotoxy(i, j);
            cout << char(219);

        }
    }
    for (int i = 142; i <= 151; i++)
    {
        for (int j = 49; j <= 50; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 144; i <= 149; i++)
    {
        for (int j = 51; j <= 51; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    gotoxy(146, 36);
    cout << "L";

    //gotoxy(20, 3);
    //cout << "X";
    //gotoxy(29, 3);
    //cout << "X";
    //gotoxy(20, 48);
    //cout << "Y";
    //gotoxy(29, 48);
    //cout << "Y";
    //gotoxy(30, 32);
    //cout << "Z";
    //gotoxy(33, 32);
    //cout << "Z";
    //gotoxy(30, 48);
    //cout << "Z";
    //gotoxy(33, 48);
    //cout << "Z";
    //gotoxy(22, 49);
    //cout << "G";
    //gotoxy(31, 49);
    //cout << "G";
    //gotoxy(22, 50);
    //cout << "G";
    //gotoxy(31, 50);
    //cout << "G";
    //gotoxy(24, 51);
    //cout << "H";
    //gotoxy(29, 51);
    //cout << "H";

}
void ColorBackground_G(int color) //sets the color of background key G
{
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsole, color);
    for (int i = 92; i <= 99; i++)
    {
        for (int j = 3; j <= 31; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 88; i <= 103; i++)
    {
        for (int j = 32; j <= 48; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 90; i <= 101; i++)
    {
        for (int j = 49; j <= 49; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 92; i <= 101; i++)
    {
        for (int j = 50; j <= 50; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 94; i <= 97; i++)
    {
        for (int j = 51; j <= 51; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    gotoxy(96, 36);
    cout << "H";
    /*gotoxy(92, 3);
    cout << "X";
    gotoxy(99, 3);
    cout << "X";
    gotoxy(92, 31);
    cout << "X";
    gotoxy(99, 31);
    cout << "X";*/
    /*gotoxy(88, 32);
    cout << "X";
    gotoxy(103, 32);
    cout << "X";
    gotoxy(88, 48);
    cout << "X";
    gotoxy(103, 48);
    cout << "X";*/


}
void ColorBackground_A(int color) //sets the color for the background of key A
{
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsole, color);
    for (int i = 110; i <= 117; i++)
    {
        for (int j = 3; j <= 31; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 106; i <= 121; i++)
    {
        for (int j = 32; j <= 48; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 108; i <= 119; i++)
    {
        for (int j = 49; j <= 49; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 108; i <= 117; i++)
    {
        for (int j = 50; j <= 50; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 112; i <= 115; i++)
    {
        for (int j = 51; j <= 51; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    gotoxy(114, 36);
    cout << "J";
}
void ColorBackground_B(int color) //sets the color of the background for key B
{
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsole, color);
    for (int i = 128; i <= 137; i++)
    {
        for (int j = 3; j <= 3; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 128; i <= 135; i++)
    {
        for (int j = 4; j <= 31; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 124; i <= 135; i++)
    {
        for (int j = 32; j <= 48; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 126; i <= 133; i++)
    {
        for (int j = 49; j <= 50; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 128; i <= 131; i++)
    {
        for (int j = 51; j <= 51; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    gotoxy(130, 36);
    cout << "K";

}
void ColorBackground_F(int color) //sets the background color for key F
{
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsole, color);
    for (int i = 72; i <= 81; i++)
    {
        for (int j = 3; j <= 31; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 72; i <= 85; i++)
    {
        for (int j = 32; j <= 48; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 72; i <= 83; i++)
    {
        for (int j = 49; j <= 49; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 76; i <= 83; i++)
    {
        for (int j = 50; j <= 50; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 76; i <= 81; i++)
    {
        for (int j = 51; j <= 51; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }
    }
    for (int i = 70; i <= 71; i++)
    {
        for (int j = 3; j <= 3; j++)
        {
            gotoxy(i, j);
            cout << char(219);
        }

    }
    gotoxy(79, 36);
    cout << "g";
}


void ::Piano::DrawPiano(string file) { //function to draw piano interface 
    int counter = 0;
    int value;
    ifstream inter;
    inter.open("C:\\Temp\\PianoDisplay.txt"); //this is the file for the piano interface

    system("cls");
    while (!inter.eof()) {
        inter >> value;
        cout << char(value);
        counter++;
        if (counter == 210) {
            cout << endl;
            counter = 0;
        }
    }
    inter.close();

}

void ::Piano::LoadNotes(string filename) { //This will take the notes from the file and store them in an array 
    char note;
    ifstream input_file(filename);
    if (!input_file.is_open())
    {
        cerr << "Unable to open "
            << filename << "" << endl;
        return;
    }
    while (input_file.get(note))
    {
        notes += note;
    }
    input_file.close();
    string file;
    DrawPiano(string(file)); //calls the DrawPiano function to draw the piano interface
}


void ::Piano::PlayNotes() { //the play notes function provided by the professor with slight modifications 
    for (char note : notes)
    {
        ShowConsoleCursor(false);
        //do re mi fa sol la si do re mi fa sol
        if (note == 'a') {
            ColorBackground_C4(14);//this will allow the program to display the background color when the note is played 
            Beep(261, 500);
            ColorBackground_C4(0); //this will blacken the background color 
        }
        if (note == 's') {
            Beep(293, 500);
        }
        if (note == 'd') {
            Beep(329, 500);
        }
        if (note == 'f') {
            Beep(349, 500);
        }
        if (note == 'g') {
            ColorBackground_F(14);
            HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE); //changes color of text to display the note 
            SetConsoleTextAttribute(hConsole, 219);
            gotoxy(79, 36); //sets cursor position 
            cout << "g"; //displays the note being played from the file 
            Beep(392, 500);
            ColorBackground_F(0); //sets background color to black 


        }
        if (note == 'h') {
            ColorBackground_G(14); //this will allow the program to display the background color when the note is played 
            HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE); //changes color of text to display the note 
            SetConsoleTextAttribute(hConsole, 219);
            gotoxy(96, 36);
            cout << "H";
            Beep(440, 500);
            ColorBackground_G(0);

        }
        if (note == 'j') {
            ColorBackground_A(14);
            gotoxy(114, 36);
            HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
            SetConsoleTextAttribute(hConsole, 219);
            cout << "J";
            Beep(493, 500);
            ColorBackground_A(0);

        }
        if (note == 'k') {
            ColorBackground_B(14);
            gotoxy(130, 36);
            HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
            SetConsoleTextAttribute(hConsole, 219);
            cout << "K";
            Beep(523, 500);
            ColorBackground_B(0);
        }
        if (note == 'l') {

            ColorBackground_C5(14);
            HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
            SetConsoleTextAttribute(hConsole, 219);
            gotoxy(146, 36);
            cout << "L";
            Beep(587, 500);
            ColorBackground_C5(0);

        }
        if (note == ';') {
            Beep(659, 500);
        }
        if (note == '\'') {
            Beep(698, 500);
        }
        if (note == '\\') {
            Beep(784, 500);
        }

        //rebemol mibemol solbemol labemol sibemol rebemol mibemol solbemol
        if (note == 'w') {
            Beep(277, 500);
        }
        if (note == 'e') {
            Beep(311, 500);
        }
        if (note == 't') {
            Beep(370, 500);
        }
        if (note == 'y') {
            Beep(415, 500);
        }
        if (note == 'u') {
            Beep(466, 500);
        }
        if (note == 'o') {
            Beep(554, 500);
        }
        if (note == 'p') {
            Beep(622, 500);
        }
        if (note == ']') {
            Beep(740, 500);
        }
    }
    gotoxy(60, 60); //sets cursor position 
}
void main() //main function 
{

    Piano mypiano; //object created 

    mypiano.LoadNotes("C:\\Temp\\mynotes.txt"); //this will load the notes from mypiano.txt

    mypiano.PlayNotes(); //this function will play the notes 



}
