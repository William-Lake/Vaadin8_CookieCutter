package {{ cookiecutter.package_path }}.ui;

import javax.servlet.annotation.WebServlet;

import org.springframework.web.bind.annotation.RequestMapping;

import com.vaadin.annotations.VaadinServletConfiguration;
import com.vaadin.server.VaadinRequest;
import com.vaadin.server.VaadinServlet;
import com.vaadin.spring.annotation.SpringUI;
import com.vaadin.ui.Label;
import com.vaadin.ui.UI;
import com.vaadin.ui.VerticalLayout;

@RequestMapping(value="/")
@SpringUI
public class PrimaryUI extends UI
{
	// TODO Generate serialVersionUID

	private VerticalLayout vlContainer;

	private Label lblTest;

	@Override
	protected void init(VaadinRequest request)
	{
		vlContainer = new VerticalLayout();

		vlContainer.setWidth("100%");

		lblTest = new Label("Test Output");

		vlContainer.addComponent(lblTest);

		setContent(vlContainer);
	}

	@WebServlet(urlPatterns = "/*", name = "MyUIServlet", asyncSupported = true)
	@VaadinServletConfiguration(ui = PrimaryUI.class, productionMode = false)
	public static class MyUIServlet extends VaadinServlet
	{

		// TODO Generate serialVersionUID
	}

}
