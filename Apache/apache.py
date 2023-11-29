from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

# Definir las configuraciones del DAG
default_args = {
    'owner': 'Aldo',
    'start_date': datetime(2023, 10, 16),
    'retries': 1,
}
# Crear un objeto DAG
dag = DAG('mi_primer_dag', default_args=default_args, schedule_interval=None)

# Definir las tareas del DAG
start_task = DummyOperator(task_id='inicio', dag=dag)
def tarea_uno():
    print("Ejecutando tarea uno")

tarea_uno_task = PythonOperator(
    task_id='tarea_uno',
    python_callable=tarea_uno,
    dag=dag
)
def tarea_dos():
    print("Ejecutando tarea dos")

tarea_dos_task = PythonOperator(
    task_id='tarea_dos',
    python_callable=tarea_dos,
    dag=dag
)

end_task = DummyOperator(task_id='fin', dag=dag)

# Definir las dependencias entre las tareas
start_task >> tarea_uno_task >> tarea_dos_task >> end_task
