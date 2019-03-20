pipeline {
    agent {
    // Equivalent to "docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
    dockerfile {
        filename 'Dockerfile.dev'
        label 'kunwarluthera/python-jenkins-flask'
    }
}
    stages {
        stage('Test') {
            steps {
                sh 'docker run -d kunwarluthera/python-jenkins-flask python app.py -- --coverage'
            }
        }
    }
}