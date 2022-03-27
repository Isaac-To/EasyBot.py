#include <iostream>
#include <string>
#include <list>

using namespace std;

class pythonlike {
public:
    string input() {
        string return_data;
        getline(cin, return_data);
        return return_data;
    }

    void print(string input_data) {
        cout << input_data << endl;
    }
};

class python {
private:
    int tabs = 2;
    string tab_me() {
        string output_data;
        for (int i = 0; i < tabs; i++) {
            output_data = output_data + "\t";
        };
        return output_data;
    };
public:
    string output(string input_data) {
        return tab_me() + "await ctx.send(f'" + input_data + "')\n";
    };
    string input(string variable_name, bool isfloat) {
        if (isfloat) {
            return tab_me() + "msg = await self.bot.wait_for('message', timeout = 10)\n" + tab_me() + variable_name + " = float(msg.content)\n";
        }
        else {
            return tab_me() + "msg = await self.bot.wait_for('message', timeout = 10)\n" + tab_me() + variable_name + " = msg.content\n";
        }
    };
    string loop(string repeats) {
        string output = tab_me() + "for i in range(0, " + repeats + "):\n";
        tabs++;
        return output;
    };
    string leave_loop() {
        string output = tab_me() + "break\n";
        tabs--;
        return output;
    }
    string math(string operation, string var_name) {
        return tab_me() + var_name + "=" + operation + "\n";
    };
    string newvar(string var_name, bool isfloat, string value) {
        if (isfloat) {
            return tab_me() + var_name + "=" + value + "\n";
        }
        else {
            return tab_me() + var_name + "=f'" + value + "'\n";
        }
    }
    string custompython(string command) {
        return tab_me() + command + "\n";
    }
    string end(string category) {
        return "def setup(bot):\n\
    \tbot.add_cog(" + category + "(bot))";
    }
};

int main()
{
    pythonlike pylike;
    pylike.print("-----Welcome to easybot.py cogs maker!-----");
    string filename;
    pylike.print("What is the category the command will be placed in?");
    string category = pylike.input();
    pylike.print("What is the name of the command?");
    string name_of_command = pylike.input();
    pylike.print("What will the command do?");
    string command_description = pylike.input();
    string fileformat = "import discord\n\
from discord.ext import commands\n\
class " + category + "(commands.Cog):\n\
\tdef __init__(self, bot):\n\
\t\tself.bot = bot\n\
\t@commands.command(name='" + name_of_command + "', help='" + command_description + "')\n\
\tasync def " + name_of_command + "(self, ctx):\n";
    python py;
    string backup[2] = {};
    while (true) {
        pylike.print("---------Program Code----------");
        pylike.print(fileformat);
        string questionaire = "What do you want to do? (If you don't know what to do; type help)";
        pylike.print(questionaire);
        backup[0] = backup[1];
        backup[1] = fileformat;
        string call = pylike.input();
        if (call == "output") {
            pylike.print("What do you want the bot to say? (You can place a variable here by using {} to surround it's name)");
            fileformat = fileformat + py.output(pylike.input());
        }
        else if (call == "input") {
            pylike.print("What do you want to name the variable?");
            string var = pylike.input();
            pylike.print("Will this variable be a number? Enter YES or NO");
            string isfloat_string = pylike.input();
            bool isfloat = false;
            if (isfloat_string == "YES") {
                bool isfloat = true;
            }
            fileformat = fileformat + py.input(var, isfloat);
        }
        else if (call == "loop") {
            pylike.print("How many times do you want to repeat? (You can use an int variable here as an alternitive)");
            fileformat = fileformat + py.loop(pylike.input());
        }
        else if (call == "leave loop") {
            fileformat = fileformat + py.leave_loop();
        }
        else if (call == "math") {
            pylike.print("Specify the operator that you want to use e.g., *, /, +, - and the two numbers you wish to compute such as 1+1 or 2*4 or 3/6; Variables can be used in place of the numbers");
            string operation = pylike.input();
            pylike.print("What is the name of the variable in which you want to store this?");
            string var = pylike.input();
            fileformat = fileformat + py.math(operation, var);
        }
        else if (call == "new variable") {
            pylike.print("What is the new variable name?");
            string var = pylike.input();
            pylike.print("Will this contain a number? Enter YES or NO");
            string type_s = pylike.input();
            bool isfloat = false;
            if (type_s == "YES") {
                isfloat = true;
            }
            pylike.print("What is it's value?");
            string value = pylike.input();
            fileformat = fileformat + py.newvar(var, isfloat, value);
        }
        else if (call == "end") {
            fileformat = fileformat + py.end(category);
            break;
        }
        else if (call == "help") {
            pylike.print("output|Sends a message to the channel\n\
input|Waits for a response\n\
loop|Repeats the script a specified amount of times\n\
leave loop|Breaks the loop before it completes the specified amount of times\n\
math|Allows you to calculate things between numbers and or variables\n\
new variable|Lets you make a new variable to store information\n\
end|To apply the end of the code and stop the program; This program does NOT save data and cannot reopen a file. Make sure you copy the final code before closing\n\
undo|To undo the last change made\n\
custompython|To add your own line of custom python\n");
        }
        else if (call == "undo") {
            fileformat = backup[0];
        }
        else if (call == "custompython") {
            pylike.print("Enter your custom python below: This does not support multiline inputs.");
            py.custompython(pylike.input());
        }
    }
    pylike.print("---------Final Code----------");
    pylike.print("This program does NOT save data and cannot reopen a file. Make sure you copy the final code before closing");
    pylike.print("Copy the code below into a new file that ends with .py and place the file you created into the .cogs folder of your easybot.py setup by chisaku-dev");
    pylike.print("----------COPY HERE----------");
    pylike.print(fileformat);
    pylike.print("-----------END HERE----------");
    pylike.input();
}
