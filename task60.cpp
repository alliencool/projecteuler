#include <cstdlib>
#include <iostream>

#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

set<int> eratosthene(int v_size)
{
    vector<int> num(v_size, 0);
    set<int> result;
    num[0] = num[1] = 1;
    for (long long i = 2; i < v_size;i++)
        if (num[i] == 0)
        {
            for (long long j = i * i; j < v_size; j += i)
                num[j] = 1;
            result.insert(i);
        }
    return result;
}

bool is_in_set(set<int>& s, int n)
{
    return s.find(n) != s.end();
}

int vec_sum(vector<int>& vec, int last_ind)
{
    int sum = 0;
    for (int i = 0; i <= last_ind; i++)
        sum += vec[i];
    return sum;
}

vector<int> take_from;
vector<int> compare_with;
map<int, vector<int> > paired_bigger;
map<int, set<int> > paired_primes;
int key;

void get_result(int start_ind, int last_ind, int depth)
{
    if (depth == -1)
    {
        cout<<"Result is";
        for (int i = 0; i <= last_ind; i++)
            cout<<" "<<compare_with[i];
        cout<<endl;

        cout<<"Sum = "<<(vec_sum(compare_with, last_ind) + key)<<endl;
    }
    else
    {
        bool flag;
        for(int i = start_ind; i < take_from.size(); i++)
        {
            flag = true;
            for (int j = 0; j <= last_ind && flag; j++)
                if (!is_in_set(paired_primes[compare_with[j]], take_from[i]))
                    flag = false;

            if (flag)
            {
                compare_with[last_ind + 1] = take_from[i];
                get_result(i + 1, last_ind + 1, depth - 1);
            }
        }
    }

}

int main(int argc, char* argv[])
{
    int MAX = 1000000;
    int DEPTH = 1;
    if (argc > 1)
    {
        MAX = atoi(argv[1]);
    }
    if (argc > 2)
    {
        DEPTH = atoi(argv[2]);
    }

    set<int> primes_s = eratosthene(MAX);

    char buffer[10];
    int a, b;
    string last;

    for(set<int>::iterator si = primes_s.begin(); si != primes_s.end(); si++)
    {
        sprintf(buffer, "%d", (*si));
        last = string(buffer);

        for (int i = 0 ;i < last.size() - 1; i++)
            if (last[i + 1] != '0')
            {
                a = atoi(last.substr(0, i + 1).c_str());
                b = atoi(last.substr(i + 1).c_str());
                if (is_in_set(primes_s, a) && is_in_set(primes_s, b))
                {
                    if (is_in_set(paired_primes[a], -b))
                    {
                        paired_primes[a].insert(b);
                        if (a < b) paired_bigger[a].push_back(b);
                    }
                    else
                        paired_primes[a].insert(-b);

                    if (is_in_set(paired_primes[b], -a))
                    {
                        paired_primes[b].insert(a);
                        if (b < a) paired_bigger[b].push_back(a);
                    }
                    else
                        paired_primes[b].insert(-a);
                }
            }
    }

    for(set<int>::iterator si = primes_s.begin(); si != primes_s.end(); si++)
    {
        take_from = paired_bigger[*si];
        compare_with = vector<int> (DEPTH + 10, 0);
        key = *si;
        get_result(0, -1, DEPTH);
    }

    return 0;
}
