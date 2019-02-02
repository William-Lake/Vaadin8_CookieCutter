package {{ cookiecutter.project_path }};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class {{ cookiecutter.project_name }} {

	public static void main(String[] args) {
		SpringApplication.run({{ cookiecutter.project_name }}.class, args);
	}

}

