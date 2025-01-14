﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Public Player class connected to Unit, Stats, Attack
public class Player: Unit, IStats
{
    private string m_name;
    private int m_Lvl = 1;
    private int m_hp;
    private int m_Armor;
    private int m_XP = 0;
    private string m_Type;

    private List<Player> m_Party = new List<Player>();

    public Player()
    {

    }
    //Player class with stats of the player
    public Player(string name, int hp, int Amr, string t)
    {
        m_name = name;
        Lvl = m_Lvl;
        m_hp = hp;
        m_Armor = Amr;
        XP = m_XP;
        Type = t;
        Life = true;
    }
    //Level/Upgrades
    //public int Upgrade1
    //{
    //    get
    //    {
    //        return m_Lvl;
    //    }
    //    set
    //    {
    //        m_Lvl = value;
    //    }
    //}
    ////Health
    //public int hp
    //{
    //    get
    //    {
    //        return m_hp;
    //    }
    //    set
    //    {
    //        m_hp = value;
    //    }
    //}
    ////Armor
    //public int  Amr
    //{
    //    get
    //    {
    //        return m_Armor;
    //    }
    //    set
    //    {
    //        m_Armor = value;
    //    }
    //}
    ////Experience
    //public int Exp
    //{
    //    get
    //    {
    //        return m_XP;
    //    }
    //    set
    //    {
    //        m_XP = value;
    //    }
    //}
    ////Name of player.
    //public string Name
    //{
    //    get
    //    {
    //        return m_name;
    //    }
    //}
    //public bool Alive(Enemy e)
    //{
    //    if(e.hp < 0)
    //    {
    //        //statement here
    //        return true;
    //    }
    //    else
    //    {
    //        //statement here
    //        return false;
    //    }
    //}
    ////checks to see if combat is active. Has if to check
   
    ////Ding Level Up
    //public void Ding()
    //{
    //    if (this.Exp == 50)
    //    {
    //        Console.Write("Your character stats have updated!\n");
    //        this.Upgrade1++;
    //        this.Exp = 0;
    //        this.hp += 15;
    //        this.Armor += 5;
    //    }
    //}
    public List<Player> Party
    {
        get
        {
            return m_Party;
        }
        set
        {
            m_Party = value;
        }
    }
}