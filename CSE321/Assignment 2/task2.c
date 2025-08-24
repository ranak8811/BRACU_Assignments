#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

int student_id = 0;
int waiting_chairs[3] = {-1, -1, -1};
int n_stds_waiting = 0;
int n_served_students = 0;
int n_stds_left = 0;

pthread_mutex_t m;
sem_t s_sem, t_sem;

void *students_management(void *arg) {
    sleep((rand() % 2) + 1);
    
    pthread_mutex_lock(&m);
    
    if (n_stds_waiting < 3) {
        printf("Student %d started waiting for consultation.\n\n", student_id);
        waiting_chairs[n_stds_waiting] = student_id;
        
        n_stds_waiting++;
        student_id++;
        
        sem_post(&s_sem);
        pthread_mutex_unlock(&m);
        sem_wait(&t_sem);
    }
    else if (n_stds_waiting == 3) {
        printf("No chairs remaining in lobby. Student %d Leaving.....\n\n", student_id);
        student_id++;
        n_stds_left++;
        pthread_mutex_unlock(&m);
    }
    
    return NULL;
}

void *st_consultation_management(void *arg) {
    while (1) {
        sem_wait(&s_sem);
        
        pthread_mutex_lock(&m);
        printf("A waiting student started getting consultation.\n");
        int student = waiting_chairs[0];
        
        waiting_chairs[0] = waiting_chairs[1];
        waiting_chairs[1] = waiting_chairs[2];
        waiting_chairs[2] = -1;
        
        n_stds_waiting--;
        
        printf("Number of students now waiting: %d\n", n_stds_waiting);
        printf("ST giving consultation\n");
        printf("Student %d is getting consultation\n\n", student);
        
        sleep(2);
        n_served_students++;
        
        printf("Student %d finished getting consultation and left\n", student);
        printf("Number of served students: %d\n\n", n_served_students);
        pthread_mutex_unlock(&m);
        
        sem_post(&t_sem);
        
        pthread_mutex_lock(&m);
        if (n_served_students + n_stds_left == 10) {
            pthread_mutex_unlock(&m);
            break;
        }
        else {
            pthread_mutex_unlock(&m);
        }
    }
    return NULL;
}

int main() {
    srand((int)getpid());
    
    pthread_t n_stds_threads[10], t_thread;
    
    pthread_mutex_init(&m, NULL);
    sem_init(&s_sem, 0, 0);
    sem_init(&t_sem, 0, 1);
    
    pthread_create(&t_thread, NULL, st_consultation_management, NULL);
    
    for (int i = 0; i < 10; i++) {
        pthread_create(&n_stds_threads[i], NULL, students_management, NULL);
    }
    
    for (int i = 0; i < 10; i++) {
        pthread_join(n_stds_threads[i], NULL);
    }
    
    pthread_join(t_thread, NULL);
    
    return 0;
}
