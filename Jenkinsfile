pipeline {
    agent any
    stages {
        stage('echo variables') {
            steps {
                sh """
                echo ${env.FOOBAR}
                """
            }
        }

        stage('build') {
            steps {
                sh 'python -m unittest -v test'
            }
        }
    }
}