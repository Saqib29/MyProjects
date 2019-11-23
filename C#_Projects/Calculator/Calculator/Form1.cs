using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calculator
{
    public partial class Form1 : Form
    {
        Double resultvalue = 0;
        string OperationPerformed = "";
        bool isOperationPerformed = false;
        public Form1()
        {
            InitializeComponent();
        }

        private void NumberButtons(object sender, EventArgs e)
        {
            Button button = (Button)sender;
            if((ResultBox.Text == "0") || isOperationPerformed)
            {
                ResultBox.Text = "";
            }
            if (button.Text == ".")
            {
                if (ResultBox.Text.Contains(".")) { }
                else
                {
                    if (ResultBox.Text.Length == 0)
                        ResultBox.Text = "0";
                    ResultBox.Text = ResultBox.Text + button.Text; 
                }
            }
            else
                ResultBox.Text = ResultBox.Text + button.Text;
            isOperationPerformed = false;
            
        }

        private void Operators(object sender, EventArgs e)
        {
            Button button = (Button)sender;
            if (!isOperationPerformed)
            {
                if (resultvalue != 0)
                {
                    button16.PerformClick();
                    isOperationPerformed = true;
                    OperationPerformed = button.Text;
                    CurrenOperation.Text = (ResultBox.Text + OperationPerformed).ToString();
                    resultvalue = Double.Parse(ResultBox.Text);
                }
                else
                {
                    isOperationPerformed = true;
                    OperationPerformed = button.Text;
                    CurrenOperation.Text = (ResultBox.Text + OperationPerformed).ToString();
                    resultvalue = Double.Parse(ResultBox.Text);
                }
            }
        }

        private void EqualButton(object sender, EventArgs e)
        {
            switch(OperationPerformed)
            {
                case "+":
                    ResultBox.Text = (resultvalue + Double.Parse(ResultBox.Text)).ToString();
                    break;
                case "-":
                    ResultBox.Text = (resultvalue - Double.Parse(ResultBox.Text)).ToString();
                    break;
                case "x":
                    ResultBox.Text = (resultvalue * Double.Parse(ResultBox.Text)).ToString();
                    break;
                case "/":
                    ResultBox.Text = (resultvalue / Double.Parse(ResultBox.Text)).ToString();
                    break;
                default:
                    break;
            }
            resultvalue = Double.Parse(ResultBox.Text);
            CurrenOperation.Text = "";
            isOperationPerformed = false;
            //OperationPerformed = "";
        }

        private void CE_Button(object sender, EventArgs e)
        {
            ResultBox.Text = "0";
        }

        private void C_Button(object sender, EventArgs e)
        {
            CurrenOperation.Text = "";
            resultvalue = 0;
            ResultBox.Text = "0";
        }
        /*
            "If need to remove frfom ResultBox then it will remove from last"
        */
        private void BackCursor(object sender, EventArgs e)
        {
            
            if(ResultBox.Text.Length >= 0)
            {
                if (ResultBox.Text.Length == 1)
                {
                    ResultBox.Text = "0";
                }
                else
                {
                    ResultBox.Text = ResultBox.Text.Remove(ResultBox.Text.Length- 1,1);
                }
            }
        }
        /* 
           This is for Plus-Minus...................................
           "if it's positive then will be negative otherwise will be Positive"
        */
        private void PlusMinusButton(object sender, EventArgs e)
        {
            if (Double.Parse(ResultBox.Text) > 0)
            {
                ResultBox.Text = "-" + ResultBox.Text;
            }
            else
                ResultBox.Text = (Math.Abs(Double.Parse(ResultBox.Text))).ToString();
        }
    }
}