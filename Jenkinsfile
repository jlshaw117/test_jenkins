pipeline {
    agent { docker {image 'python:2.7.16' } }
    stages {
        stage('echo variables') {
            sh """
            echo ${env.FOOBAR}
            """
        }

        stage('build') {
            steps {
                sh 'python -m unittest -v test'
            }
        }
    }
}