pipeline {
    agent {
    // Equivalent to "docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
    dockerfile true
}
    stages {
        stage('Test') {
            steps {
                sh 'echo hello world'
            }
        }
    }
}