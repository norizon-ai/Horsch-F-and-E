# Queue Architecture

## RabbitMQ in a Separate, Dedicated Container


   * How it Works:
       * You would have a docker-compose.yml file that defines at least two services: one for rabbitmq and one for the ingestion-worker.
       * The rabbitmq service would use an official RabbitMQ Docker image (e.g., rabbitmq:3-management).
       * The ingestion-worker service would be built from our own Dockerfile, containing the Python environment and the worker script.
       * The two containers would communicate over a shared Docker network.


   * Pros:
       * Decoupling & Resilience (High): This is the biggest advantage. If the worker container crashes due to a bug or high memory usage
         during embedding, the RabbitMQ container is completely unaffected. Messages remain safe in the queue, ready to be processed when
         the worker restarts.
       * Scalability (High): You can scale the workers independently of the message queue. If processing becomes a bottleneck, you can
         simply run docker-compose up --scale ingestion-worker=5 to spin up five workers that consume from the same queue, without touching
         the RabbitMQ instance.
       * Resource Management: You can allocate resources (CPU, memory) to RabbitMQ and the workers separately, based on their different
         needs. RabbitMQ is typically I/O-bound, while the embedding worker will be CPU/GPU-bound.
       * Maintainability: It follows the Single Responsibility Principle. The RabbitMQ container does one thing: manage queues. The worker
         container does one thing: process data. This makes updates and debugging much simpler.


   * Cons:
       * Slightly More Complex Setup: It requires a docker-compose.yml file and a basic understanding of Docker networking (though
         docker-compose handles most of this automatically).



  This approach aligns perfectly with the principles of a robust, microservices-style architecture, which is what we are building. The
  core reason for using a message queue is to decouple services, and putting RabbitMQ in the same container as the worker completely
  undermines that benefit.


  By keeping them separate, we gain:
   1. Resilience: The system can tolerate worker failures without data loss.
   2. Scalability: We can independently scale the part of the system that needs more resources (the workers) without affecting the message
      broker.
   3. Maintainability: It's a cleaner, more professional setup that is easier to understand, update, and debug in the long run.


  The added complexity of docker-compose is minimal and is a standard best practice for managing multi-container applications.

  Implementation Sketch

  To illustrate, our docker-compose.yml file would look something like this:



    1 version: '3.8'
    2 
    3 services:
    4   rabbitmq:
    5     image: "rabbitmq:3-management"
    6     ports:
    7       - "5672:5672"  # For the worker to connect
    8       - "15672:15672" # For the web management UI
    9     volumes:
   10       - rabbitmq_data:/var/lib/rabbitmq/
   11     networks:
   12       - intranet_connector_net
   13 
   14   ingestion-worker:
   15     build: . # Assumes Dockerfile is in the same directory
   16     depends_on:
   17       - rabbitmq
   18     environment:
   19       - RABBITMQ_URL=amqp://guest:guest@rabbitmq:5672/
   20       - DATABASE_URL=...
   21     networks:
   22       - intranet_connector_net
   23 
   24 networks:
   25   intranet_connector_net:
   26     driver: bridge
   27 
   28 volumes:
   29   rabbitmq_data:



  This setup provides a solid and professional foundation for our system.