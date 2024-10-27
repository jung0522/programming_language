#include <vector>
#include <iostream>
#include <algorithm>

int main()
{
    std::vector<int> v = { 10, 20, 30, 40, 50 };
    int idx = 0;

    for_each(v.begin(), v.end(),
        [&idx](int vValue) { std::cout << "v[" << idx++ << "] = " << vValue << std::endl; vValue++; std::cout << "v[" << idx++ << "] = " << vValue << std::endl; });
    std::cout << "idx = " << idx << std::endl;

    return 0;
}