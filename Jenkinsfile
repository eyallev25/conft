pipeline {
    agent any

    stages {
        

        stage('Build') {
            steps {
                // Build the Python script (replace with your build commands)
                
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Script') {
            steps {
                // Run the Python script (replace with your script's name)
                sh 'python my_script.py'
            }
        }
    }

    post {
        success {
            // This block runs if the pipeline succeeds
            echo 'Pipeline successful!'
        }
        failure {
            // This block runs if the pipeline fails
            echo 'Pipeline failed!'
        }
    }
}
