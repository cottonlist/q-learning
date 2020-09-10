#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>

void crash(){
	printf("crash\n");
}

struct State{
	int id;
	struct State *left;
	struct State *right;
};

struct State states[10];

int num_of_state = 1;
int current_trace = 0;

void create_state(int thread_id){

	int flag = 1;

	current_trace = current_trace * 10 + thread_id;

	for (int i = 0; i < num_of_state; ++i)
	{
		if (states[i].id == current_trace)
		{
			flag = 0;
		}
	}

	if (flag == 1)
	{
		states[num_of_state++].id = current_trace;
	}

}

int a = 0;

void *
func1 (void *arg)
{
	a = 1;
	create_state(1);

	if (a == 2)
	{
		crash();
	}
	create_state(1);

	return NULL;
}

void *
func2 (void *arg)
{
	a++;
	create_state(2);

	return NULL;
}

int
main()
{
	states[0].id = 0;

	pthread_t t1;
	pthread_t t2;

	for (int i = 0; i < 100; ++i)
	{
		pthread_create(&t1, NULL, func1, NULL);
		pthread_create(&t2, NULL, func2, NULL);
		pthread_join(t1, NULL);
		pthread_join(t2, NULL);

		current_trace = 0;
	}

	printf("number of state: %d\n", num_of_state);
	for (int i = 0; i < num_of_state; ++i)
	{
		printf("State %d, id %d\n", i, states[i].id);
	}

	exit(0);
}
