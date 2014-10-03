#include <iostream>
#include <vector>
#include <set>
#include <cstdlib>

using namespace std;

vector<int> to_vec(int num)
{
    vector<int> repr;
    if (num == 0)
        repr.push_back(0);
    while (num)
    {
        repr.push_back(num % 10);
        num /= 10;
    }
    return repr;
}

int to_int(vector<int> vec)
{
    int result = 0;
    for(int i = (vec.size() - 1); i >= 0 ;i--)
        result = result * 10 + vec[i];
    return result;
}

set<int> eratosthene(int v_size)
{
    vector<int> num(v_size, 0);
    set<int> result;
    num[0] = num[1] = 1;
    for (int i = 2; i < v_size;i++)
        if (num[i] == 0)
        {
            for (int j = i + i; j < v_size; j += i)
                num[j] = 1;
            result.insert(i);
        }
    return result;
}

void print_set(set<int> s)
{
    for (set<int>::iterator it = s.begin(); it != s.end(); it++)
        cout<<(*it)<<endl;
}

void print_vec(vector<int> v)
{
    for (vector<int>::iterator it = v.begin(); it != v.end(); it++)
        cout<<(*it)<<endl;
}

vector<int> get_positions(int num)
{
    vector<int> result;
    for (int i = 0; i < 32;i++)
    {
        if (num & (1<<i))
            result.push_back(i);
    }
    return result;
}

bool is_equal(vector<int> positions, int num)
{
    vector<int> n=to_vec(num);
    int prev = -1;
    for(vector<int>::iterator it=positions.begin(); it != positions.end(); it++)
    {
       if (prev == -1)
           prev = n[*it];
       else if ( prev != n[*it] )
           return false;
    }
    return true;
}

int main(int argc, char* argv[])
{
    int MAX = 100;
    int amount = 6;
    if (argc >= 2)
    {
        MAX = atoi(argv[1]);
    }
    if (argc >= 3)
    {
        amount = atoi(argv[2]);
    }
    set<int> primes_s = eratosthene(MAX);
    for(set<int>::iterator it = primes_s.begin(); it != primes_s.end(); it++)
    {
        int prime = (*it);
        vector<int> positions;
        vector<int> prime_v=to_vec(prime);
        int pos = prime_v.size();
        int pw = 1 << (pos);
        //cout<<"DEBUG 0. Prime "<<prime<<" pw="<<pw<<" pos"<<pos<<endl;
        for (int i = 1 ; i < pw; i++)
        {
            positions = get_positions(i);
            if (is_equal(positions, prime) && prime_v[positions[0]] <= (10 - amount))
            {
                vector<int> vec = prime_v;
                int c = 1;
                vector<int> result;
                result.clear();
                //cout<<"DEBUG 1. Content of positions:"<<endl;
                //print_vec(positions);
                while (vec[positions[0]] < 9)
                {
                    //cout<<"DEBUG 2. Content of vec. BEFORE"<<endl;
                    //print_vec(vec);
                    for (int p = 0; p < positions.size();p++)
                    {
                        //cout<<"INSIDE "<<positions.size()<<" "<<p<<endl;
                        //cout<<"BEFORE "<<vec[positions[p]];
                        vec[positions[p]] += 1;
                        //cout<<" AFTER "<<vec[positions[p]]<<endl;
                    }
                    //cout<<"DEBUG 2 AFTER"<<endl;
                    //print_vec(vec);
                    if (primes_s.find(to_int(vec)) != primes_s.end())
                    {
                        c++;
                        result.push_back(to_int(vec));
                    }
                }
                if (c >= amount)
                {
                    cout<<"Answer is "<<prime<<" .Amount is "<<c<<" . Reference amount is "<<amount<<endl;
                    print_vec(result);
                }
            }
        }
    }
    return 0;
}
