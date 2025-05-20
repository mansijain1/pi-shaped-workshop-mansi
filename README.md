# pi-shaped-workshop-mansi
1. Why is Docker useful in building and deploying microservices for a real-world product (like an e-commerce or banking app)?

    * Consistent Setup – Ensures the app runs the same on all machines and environments.
    * Independent Services – Each microservice lives in its own container, reducing interference.
    * Efficient and Lightweight – Uses fewer resources and starts up quickly.
    * Flexible Scaling – Allows you to scale only the services that need more capacity.
    * Improved Reliability – Issues in one service won’t affect the rest of the system.
    * Cross-Platform Support – Runs smoothly on any cloud, OS, or infrastructure.

2. What is the difference between a Docker image and a container in the context of scaling a web application?

    A Docker image is a static blueprint or template that defines everything needed to run an application, such as code, dependencies, and configuration. Once built the image remains unchanged and can be used to create multiple identical environments. 

   While, a Docker container is a dynamic, running instance of that image. It has a runtime state and can change during execution. 
    When scaling a web application, You only need to build the image once, and then launch multiple containers from it to handle increased traffic, making containers the actual units scaled across the system.

4. How does Kubernetes complement Docker when running a product at scale (e.g., hundreds of containers)?

   * Container Orchestration: Docker runs individual containers, while Kubernetes manages and orchestrates containers at scale.
   * Automated Scaling: Kubernetes automatically adjusts the number of containers based on demand.
   * Load Balancing: Distributes traffic across containers to ensure high availability and prevent overload.
   * Self-Healing: Restarts or replaces containers if they fail to maintain desired state.
   * Rolling Updates: Deploys updates without downtime and can roll back if needed.
   * Service Discovery: Automatically manages container communication within the cluster.
   * Resource Management: Allocates CPU, memory, and storage efficiently across containers.

