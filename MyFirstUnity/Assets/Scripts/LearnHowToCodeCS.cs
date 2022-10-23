using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LearnHowToCodeCS : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        MyPlayer warrior = new MyPlayer(10, 20, "warrior");
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private IEnumerator DelaySomething()
    {
        yield return new WaitForSeconds(seconds: 2f);
        Debug.Log("something is printed!!!");
    }
}
