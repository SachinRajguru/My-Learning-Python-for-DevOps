# Jenkins Pipeline

Pipeline {
    agent any {
        stages {
            stage('Build') {
                steps {
                    echo 'Building'
                }
            }
            stage('Test') {
                echo 'Testing'
            }
        }
    }
}

