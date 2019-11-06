using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Sudoku
{
    public partial class Form1 : Form
    {
        public int[,] Werte = new int[9,9];//row und dann spalte  fertige Werte
        public List<int>[][] posiblWerte;//enthät alle noch möglichen werten index1= row index2 = spalte
       
        #region "Events"
        private void Form1_Load(object sender, EventArgs e)
        {
            for (int i = 0; i < 9; i++)
            {
                dgv.Rows.Add();
                dgv.Rows[i].HeaderCell.Value = i.ToString();
            }

        }
        public Form1()
        {
            InitializeComponent();
        }

        private void b_Laden_Click(object sender, EventArgs e)
        {
            Load_Standard_Sudokuwerte();
            Show_werte();
        }
        private void b_Solve_Click(object sender, EventArgs e)
        {
            Load_posWerte();
            for (int loops = 0; loops < 65; loops++)
            {
                for (int i = 0; i < 9; i++)
                {
                    for (int j = 0; j < 9; j++)
                    {
                        Update_posWerte(i, j);
                    }
                }
            }
            Show_werte();
        }
        private void b_Loop_Click(object sender, EventArgs e)
        {
            for (int loops = 0; loops < 100; loops++)
            {
                for (int i = 0; i < 9; i++)
                {
                    for (int j = 0; j < 9; j++)
                    {
                        Update_posWerte(i, j);
                    }
                }
            }
            Show_werte();
        }
        private void b_load_manuell_Click(object sender, EventArgs e)
        {
            for (int i = 0; i < 9; i++)
            {
                for (int j = 0; j < 9; j++)
                {
                    int resutint;
                    bool resultb = int.TryParse(dgv[j, i].Value.ToString(),out resutint);
                    if (resultb)
                    {
                        if (resutint > -1 && resutint < 10)
                        {
                            Werte[i, j] = resutint;
                        }
                        else
                        {
                            MessageBox.Show("Unültige Feldeingabe: " + dgv[j, i].Value.ToString() + " bei Index:" + i.ToString() + ";" + j.ToString());
                            return;
                        }
                    }
                    else
                    {
                        if (dgv[j, i].Value.ToString() == "")
                        {
                            Werte[i, j] = 0;
                        }
                        else
                        {
                            MessageBox.Show("Unültige Feldeingabe: " + dgv[j, i].Value.ToString() + " bei Index:" + i.ToString() + ";" + j.ToString());
                            return;
                        }
                    }
                }
            }
        }
        private void b_Reset_Click(object sender, EventArgs e)
        {
            Load_posWerte();
            for (int i = 0; i < 9; i++)
            {
                for (int j = 0; j < 9; j++)
                {
                    Werte[i, j] = 0;
                }
            }
            Show_werte();
        }
        #endregion

        #region "Hilfsfunktionen"
        private void Load_Standard_Sudokuwerte()
        {
            for (int i = 0; i < 9; i++)
            {
                for (int j = 0; j < 9; j++)
                {
                    Werte[i, j] = 0;
                }
            }
            Werte[0, 2] = 8;
            Werte[0, 6] = 9;
            Werte[1, 1] = 6;
            Werte[1, 2] = 2;
            Werte[1, 4] = 9;
            Werte[1, 5] = 8;
            Werte[1, 7] = 3;
            Werte[2, 2] = 9;
            Werte[2, 3] = 1;
            Werte[2, 4] = 3;
            Werte[2, 7] = 8;

            Werte[3, 0] = 9;
            Werte[3, 2] = 3;
            Werte[3, 5] = 7;
            Werte[3, 7] = 6;
            Werte[3, 8] = 5;
            Werte[4, 4] = 1;
            Werte[5, 0] = 2;
            Werte[5, 1] = 5;
            Werte[5, 3] = 6;
            Werte[5, 6] = 7;
            Werte[5, 8] = 1;

            Werte[6, 0] = 7;
            Werte[6, 2] = 6;
            Werte[6, 4] = 4;
            Werte[6, 5] = 9;
            Werte[6, 7] = 5;
            Werte[6, 8] = 8;
            Werte[7, 0] = 3;
            Werte[7, 3] = 8;
            Werte[7, 5] = 1;
            Werte[7, 8] = 9;
            Werte[8, 0] = 8;
            Werte[8, 1] = 9;
            Werte[8, 2] = 1;
            Werte[8, 3] = 2;
            Werte[8, 4] = 5;
            Werte[8, 8] = 4;
        }
        private void Show_werte()
        {
            for (int i = 0; i < 9; i++)
            {
                for (int j = 0; j < 9; j++)
                {
                    if (Werte[i, j] != 0)
                    {
                        dgv.Rows[i].Cells[j].Value = Werte[i, j];
                    }
                    else
                    {
                        dgv.Rows[i].Cells[j].Value = "";
                    }
                }
            }
        }
        private void Load_posWerte()
        {
            posiblWerte = new List<int>[9][];
            for (int i = 0; i < 9; i++)
            {
                posiblWerte[i] = new List<int>[9];
                for (int j = 0; j < 9; j++)
                {
                    posiblWerte[i][j] = new List<int>();
                    for (int k = 1; k < 10; k++)
                    {
                        int saver = saver = k;
                        posiblWerte[i][j].Add(saver);
                    }
                }
            }
        }
        private void Update_posWerte(int row, int coloumn)
        {
            if (Werte[row, coloumn] > 0)
            {
                return;
            }

            //Box
            int corerow;
            int corecol;
            if (row > 5)
            {
                corerow = 7;
            }
            else if (row < 3)
            {
                corerow = 1;
            }
            else
            {
                corerow = 4;
            }

            if (coloumn > 5)
            {
                corecol = 7;
            }
            else if (coloumn < 3)
            {
                corecol = 1;
            }
            else
            {
                corecol = 4;
            }

            for (int i = -1; i < 2; i++)
            {
                for (int j = -1; j < 2; j++)
                {
                    if (Werte[corerow + i, corecol + j] != 0)
                    {
                        posiblWerte[row][coloumn].RemoveAll(value => value == Werte[corerow + i, corecol + j]);
                    }
                }
            }

            //Row
            for (int i = 0; i < 9; i++)
            {
                if (Werte[row, i] != 0)
                {
                    posiblWerte[row][coloumn].RemoveAll(value => value == Werte[row, i]);
                }
            }

            //Spalte
            for (int i = 0; i < 9; i++)
            {
                if (Werte[i, coloumn] != 0)
                {
                    posiblWerte[row][coloumn].RemoveAll(value => value == Werte[i, coloumn]);
                }
            }

            if (posiblWerte[row][coloumn].Count == 1)
            {
                int test = posiblWerte[row][coloumn][0];
                Werte[row, coloumn] = posiblWerte[row][coloumn][0];
                posiblWerte[row][coloumn].RemoveAt(0);
                //Show_werte();
                //Application.DoEvents();
            }
        }

        #endregion

        private void b_Loadfile_Click(object sender, EventArgs e)
        {
            oFD1.Multiselect = false;
            oFD1.Title = "Choose File to open";
             while (!System.IO.File.Exists(oFD1.FileName))
                {
                    oFD1.ShowDialog();
                }
            System.IO.StreamReader sr = new System.IO.StreamReader(oFD1.FileName);
            int row = 0;
            while (row < 8 && sr.Peek() != -1)
            {
                string zeile = sr.ReadLine();
                if (!string.IsNullOrEmpty(zeile))
                {
                    string[] values = zeile.Split(' ');
                    if (values.Count() == 11)
                    {
                        int steps = 0;
                        for ( int i = 0;i<9;i++)
                        {
                            if (i == 3 || i == 6)
                            {
                                steps++;
                            }
                            Werte[row, i] = Convert.ToInt32(values[i+steps]);
                        }
                        row++;
                    }
                }
               
            }
            Show_werte();
        }
    }
}
