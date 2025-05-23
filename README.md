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


DAY-2 
1. Why do we set requests and limits for CPU/memory in a production-grade product?

    * Requests ensure pods get the minimum resources they need and are scheduled properly.
    * Limits prevent any pod from using too much and affecting others.
    * It ensures stability, efficient performance, fair resource allocation, and cost optimization.

2. When would a product team apply node affinity in Kubernetes?

    Node affinity is used when you want to schedule pods on specific nodes based on labels — for reasons like hardware needs, environment isolation, or performance tuning.

DAY-3

1. How would you expose an internal microservice (e.g., user-auth) differently than a public-facing frontend in a Kubernetes-based product?

    In Kubernetes, internal microservices like user-auth are typically exposed using ClusterIP services, making them accessible only within the cluster for security and control. In contrast, public-facing services like a frontend are exposed via Ingress or LoadBalancer, allowing external user access while enabling security measures like TLS and routing rules.

2. Why might a product use Ingress instead of directly exposing each microservice via LoadBalancer?

    To reduce costs and resource usage, as Ingress allows multiple services to share a single external IP. 
    It also provides centralized routing, TLS termination, and traffic management, making it easier to manage and secure external access.