package {{ cookiecutter.package_path }}.rest;

import java.util.List;

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.GenericType;
import javax.ws.rs.core.MediaType;

public class RestClient
{
	private Client client;

	private WebTarget webTarget;

    // TODO Replace this with your REST API's base url endpoint.
    private static final String API_URL = "http://EXAMPLE_SITE.com/api/v2/";

	private static final class Wrapper
    {
        static final RestClient INSTANCE = new RestClient();
    }

    private RestClient()
    {
        // Private Constructor to create Singleton

        // ...code to ensure RestClient is working as expected...

		client = ClientBuilder.newClient();

		webTarget = client.target(API_URL);
    }

    public static RestClient getInstance()
    {
        return Wrapper.INSTANCE;
    }

    public Object getObject()
    {
        return

                webTarget
                .path("ENDPOINT_URL_PATH_SECTION")
                .request()
                .accept(MediaType.APPLICATION_JSON)
                .get(Object.class);
    }

    public List<Object> getObjects()
    {
        return

                webTarget
                .path("ENDPOINT_URL_PATH_SECTION")
                .request()
                .accept(MediaType.APPLICATION_JSON)
                .get(new GenericType<List<Object>>() {});
    }   

    public void putObject(Object object)
    {
        webTarget
        .path("ENDPOINT_URL_PATH_SECTION")
        .request(MediaType.APPLICATION_JSON)
        .put(Entity.json(object), Object.class);
    }

    public void postObject(Object object)
    {
        webTarget
        .path("ENDPOINT_URL_PATH_SECTION")
        .request(MediaType.APPLICATION_JSON)
        .post(Entity.json(object),Object.class);
    }

    public void deleteObject(Object object)
    {
        webTarget
        .path("ENDPOINT_URL_PATH_SECTION")
        .path("ANOTHER_ENDPOINT_URL_PATH_SECTION")
        .path("LIKELY THE object ID")
        .request()
        .accept(MediaType.APPLICATION_JSON)
        .delete();
    }
}