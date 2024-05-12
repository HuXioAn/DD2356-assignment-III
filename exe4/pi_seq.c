
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>

#include "mpi.h"

#define SEED     921
#define NUM_ITER 1000000000

int main(int argc, char* argv[])
{

    int provided;
    
    MPI_Init_thread(&argc, &argv, MPI_THREAD_SINGLE, &provided);

    int world_rank, world_size;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);



    int count = 0;
    double x, y, z, pi;
    
    srand(time(NULL) + world_rank * SEED); // Important: Multiply SEED by "rank" when you introduce MPI!
    
    double startTime = MPI_Wtime();
    // Calculate PI following a Monte Carlo method
    for (int iter = 0; iter < (NUM_ITER/world_size); iter++)
    {
        // Generate random (X,Y) points
        x = (double)random() / (double)RAND_MAX;
        y = (double)random() / (double)RAND_MAX;
        z = sqrt((x*x) + (y*y));
        
        // Check if point is in unit circle
        if (z <= 1.0)
        {
            count++;
        }
    }

    //reduction
    int totalCount = 0;
    MPI_Reduce(&count, &totalCount, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    if(world_rank == 0){
        // Estimate Pi and display the result
        pi = ((double)totalCount / (double)NUM_ITER) * 4.0;
        printf("The result is %f\n", pi);
        printf("The time elapsed is %f\n", MPI_Wtime()-startTime);
    }

    MPI_Finalize();
    
    return 0;
}

