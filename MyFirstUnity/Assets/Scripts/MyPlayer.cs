using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MyPlayer
{
    int heath;
    int power;
    string playerNmae;

    public MyPlayer()
    {
    }

    public MyPlayer(int heath, int power, string playerNmae)
    {
        this.heath = heath;
        this.power = power;
        this.playerNmae = playerNmae;
        Debug.Log("health is " + heath);
        Debug.Log("power is " + power);
        Debug.Log("playerNmae is " + playerNmae);
    }

    public virtual void Attack()
    {
        Debug.Log("the player is attacking with fire");
    }
}
