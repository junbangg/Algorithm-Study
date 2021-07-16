#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stdio.h>
#include <time.h>
// #include <time.h>
#define N              4
#define MAX_QUERYCOUNT 1000000

static int digits[N];
static int digits_c[10];

static int T;

// extern void doUserImplementation(int guess[]);

static int querycount; 

// the value of limit_query will be changed in evaluation
static const int limit_query = 234;

typedef struct {
	int hit;
	int miss;
} Result;
// need a function to convert 4 digit int -> size 4 array
// change to 2d
int ** createPool(int h, int w) {

    int** arr = 0;
    arr = new int*[h];

    int validDigits[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int cnt = 0;
    for (int i = 0; i < 10; i++) {
        for ( int j = 0; j < 10; j++) {
            for ( int k = 0; k < 10; k++) {
                for (int l = 0; l < 10; l++) {
                    arr[cnt] = new int[w];
                    if (i != j && i != k && i != l && j != k && j != l && k != l) {
                        arr[cnt][0] = validDigits[i];
                        arr[cnt][1] = validDigits[j];
                        arr[cnt][2] = validDigits[k];
                        arr[cnt][3] = validDigits[l];
                        cnt++;
                    };
                };
            };
        };
    };
    return arr;
};
bool checkValidity(int myGuess[]) {
	int temp[10];
	
	for (int count = 0; count < 10; ++count) temp[count] = 0;
	for (int idx = 0; idx < N; ++idx) {
		if (myGuess[idx] < 0 || myGuess[idx] >= 10 || temp[myGuess[idx]] > 0) return false;
		temp[myGuess[idx]]++;
	}
	return true;
};
Result prune(int usersGuess[], int candidate[]) {
	Result result;
    int map[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    if (!checkValidity(candidate)) {
		result.hit = -1;
		result.miss = -1;
		return result;
	}

    //count elements
    for ( int i = 0; i < N; i++) {
        map[usersGuess[i]]++;
    };
	
	result.hit = 0;
	result.miss = 0;

	for (int idx = 0; idx < N; idx++)
		if (usersGuess[idx] == candidate[idx])
			result.hit++;
		else if (map[candidate[idx]] > 0)
			result.miss++;
	return result;
}
 

static bool isValid(int guess[]) {
	int guess_c[10];
	
	for (int count = 0; count < 10; ++count) guess_c[count] = 0;
	for (int idx = 0; idx < N; ++idx) {
		if (guess[idx] < 0 || guess[idx] >= 10 || guess_c[guess[idx]] > 0) return false;
		guess_c[guess[idx]]++;
	}
	return true;
}

// API : return a result for comparison with digits[] and guess[]
Result query(int guess[]) {
	Result result;
	
	if (querycount >= MAX_QUERYCOUNT) {
		result.hit = -1;
		result.miss = -1;
		return result;
	}
	
    querycount++;
		
	if (!isValid(guess)) {
		result.hit = -1;
		result.miss = -1;
		return result;
	}
	
	result.hit = 0;
	result.miss = 0;

	for (int idx = 0; idx < N; ++idx)
		if (guess[idx] == digits[idx])
			result.hit++;
		else if (digits_c[guess[idx]] > 0)
			result.miss++;

	return result;
}

static void initialize() {
	for (int count = 0; count < 10; ++count) digits_c[count] = 0;
	for (int idx = 0; idx < N; ++idx) {
		char c;
		do scanf("%c", &c); while(c < '0' || c > '9');
		digits[idx] = c - '0';
		digits_c[digits[idx]]++;
	}
	
	querycount = 0;
}

static bool check(int guess[]) {
	for (int idx = 0; idx < N; ++idx)
		if (guess[idx] != digits[idx]) return false;
	return true;
}
// int random(int low, int high){
//     int *p;
//     p = (int*)malloc(sizeof(int));
//     int num = ((int)p%(high-low))+low;
//     return num;
// };
void doUserImplementation(int guess[]) {
           // Implement a user's implementation function
           //
           // The array of guess[] is a return array that
           // is your guess for what digits[] would be.
    int size = 5040;
    int** pool = createPool(size, N);

    int indDecision = 0;
    while (size>=1) {
        //make a guess query(random)
        // int guessIndex = indDecision++ % size;
        srand((unsigned) time(0));
        int guessIndex = rand() / size;
        int usersGuess[N];
        // copy to guess[]
        for (int i = 0; i < N; i++) {
            usersGuess[i] = pool[guessIndex][i];
        };

        Result response = query(usersGuess);
        if (response.hit == -1 && response.miss == -1) {
            continue;
        };
        // if correct
        if (response.hit == 4) {
            //copy usersGuess -> guess
            for (int i = 0; i < N; i++) {
                guess[i] = usersGuess[i];
            };
            break;
        }
        
        // delete elements that share same results
        for (int i = 0; i < size; i++) {
            Result pruned = prune(usersGuess, pool[i]);
            if (pruned.hit == -1 && pruned.miss == -1 || pruned.hit != response.hit && pruned.miss != response.miss) {
                //delete from pool
                for (int k=i; k < size - 1; k++) {
                    pool[k] = pool[k+1];
                };
                // decrease size
                size--;
            };
        };
        indDecision++;
    };
    int prunedGuess[N];
    for (int i=0; i<size; i++) {
        for(int j=0;j<N; j++) {
            prunedGuess[j] = pool[i][j];
        };
        Result final = query(prunedGuess);

        if (final.hit == 4) {
            for (int k=0;k<N;k++) {
                guess[k] = prunedGuess[k];
            };
            break;
        };
    };
    
};
int main() {
	int total_score = 0;
	int total_querycount = 0;;
	
    // freopen("sample_input.txt", "r", stdin);
	setbuf(stdout, NULL);

	scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase) {
        initialize();

        int guess[N];
		doUserImplementation(guess);

		if (!check(guess)) querycount = MAX_QUERYCOUNT;
        if (querycount <= limit_query) total_score++;
		printf("#%d %d\n", testcase, querycount);
		total_querycount += querycount;
    }
	if (total_querycount > MAX_QUERYCOUNT) total_querycount = MAX_QUERYCOUNT;
	printf("total score = %d\ntotal query = %d\n", total_score * 100 / T, total_querycount);
	return 0;
}