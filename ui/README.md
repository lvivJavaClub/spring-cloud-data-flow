# Getting started
https://cloud.spring.io/spring-cloud-dataflow/#quick-start

1. wget https://raw.githubusercontent.com/spring-cloud/spring-cloud-dataflow/v1.7.3.RELEASE/spring-cloud-dataflow-server-local/docker-compose.yml
1. DATAFLOW_VERSION=1.7.3.RELEASE docker-compose up
1. Open the dashboard at http://localhost:9393/dashboard


# Create workflow 
```
input_file: file --mode=lines --filename-pattern='*.log' --directory=/javaClub/spring-data-flow | name_filter: filter --expression=!payload.contains('Luca Cox') | output_file: file --name=jclub_names --suffix=flow --directory=/javaClub/spring-data-flow
```
# Generate random data

```
# optional
chmod +x randomName.py
./randomName.py | tee names.log
docker cp names.log dataflow-server:/javaClub/spring-data-flow
```

# Check what's in container
docker exec -it dataflow-server cls -la /javaClub/spring-data-flow/

## Input file
docker exec -it dataflow-server cat /javaClub/spring-data-flow/names.log | wc -l
docker exec -it dataflow-server grep Luca /javaClub/spring-data-flow/names.log | wc -l

## Output file
docker exec -it dataflow-server cat /javaClub/spring-data-flow/jclub_names.flow | wc -l
docker exec -it dataflow-server grep Luca /javaClub/spring-data-flow/jclub_names.flow | wc -l
