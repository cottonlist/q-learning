#include <stdio.h>
#include <stdlib.h>

struct state
{
	char *trace;
	int reward;
	struct state *left;
	struct state *right;
};

int main(int argc, char const *argv[])
{
	struct state s[20];
	s[0].trace = "0";
	s[1].trace = "1";
	s[2].trace = "2";
	s[3].trace = "11";
	s[4].trace = "12";
	s[5].trace = "21";
	s[6].trace = "112";
	s[7].trace = "121";
	s[8].trace = "211";

	for (int i = 0; i < 9; ++i)
	{
		s[i].reward = 0;
	}

	for (int i = 0; i < 6; ++i)
	{
		s[i].left = NULL;
		s[i].right = NULL;
	}

	for (int i = 0; i < 9; ++i)
	{
		for (int j = i + 1; j < 9; ++j)
		{
			int m = atoi(s[i].trace);
			int n = atoi(s[j].trace);
			if (n - 10 * m == 1)
			{
				s[i].left = &s[j];
			} else if (n - 10 * m == 2)
			{
				s[i].right = &s[j];
			}
		}
	}

	printf("%s, %s, %s\n", s[1].trace, s[1].left->trace, s[1].right->trace);

	return 0;
}