package com.example.weather_app

import android.os.AsyncTask
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.ContactsContract.CommonDataKinds.Website.URL
import android.view.View
import android.widget.ProgressBar
import android.widget.RelativeLayout
import android.widget.TextView
import org.json.JSONObject
import java.net.URL
import java.text.SimpleDateFormat
import java.util.*

class MainActivity : AppCompatActivity() {

    val CITY: String = "seoul,kr"
    val API: String = "21fc8bd696c37054a5ba3d7d13edb87f"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        weatherTask().execute()
    }
    inner class weatherTask() : AsyncTask<String, Void, String>(){
        override fun onPreExecute() {
            super.onPreExecute()
            findViewById<ProgressBar>(R.id.pbloader).visibility = View.VISIBLE
            findViewById<RelativeLayout>(R.id.rlmainContainer).visibility = View.GONE
            findViewById<TextView>(R.id.tverrorText).visibility = View.GONE
        }

        override fun doInBackground(vararg p0: String?): String? {
            var response:String?
            try{
                response = URL("https://api.openweathermap.org/data/2.5/weather?q=$CITY&units=metric&appid=$API")
                    .readText(Charsets.UTF_8)
            }
            catch (e: Exception){
                response = null
            }
            return response
        }

        override fun onPostExecute(result: String?) {
            super.onPostExecute(result)
            try{
                val jsonObj = JSONObject(result)
                val main = jsonObj.getJSONObject("main")
                val sys = jsonObj.getJSONObject("sys")
                val wind = jsonObj.getJSONObject("wind")
                val weather = jsonObj.getJSONArray("weather").getJSONObject(0)
                val updatedAt:Long = jsonObj.getLong("dt")
                val updatedAtText = "Updated at: " + SimpleDateFormat("MM/dd/yyyy hh:mm a", Locale.ENGLISH).format(Date(updatedAt*1000))
                val temp = main.getString("temp")+"°C"
                val tempMin = "Min Temp: " + main.getString("temp_min")+"°C"
                val tempMax = "Max Temp: " + main.getString("temp_max")+"°C"
                val pressure = main.getString("pressure")
                val humidity = main.getString("humidity")
                val sunrise:Long = sys.getLong("sunrise")
                val sunset:Long = sys.getLong("sunset")
                val windSpeed = wind.getString("speed")
                val weatherDescription = weather.getString("description")
                val address = jsonObj.getString("name") + ", "+sys.getString("country")

                findViewById<TextView>(R.id.tvaddress).text = address
                findViewById<TextView>(R.id.tvupdatedAt).text = updatedAtText
                findViewById<TextView>(R.id.tvstatus).text = weatherDescription.capitalize()
                findViewById<TextView>(R.id.tvtemp).text = temp
                findViewById<TextView>(R.id.tvtempMin).text = tempMin
                findViewById<TextView>(R.id.tvtempMax).text = tempMax
                findViewById<TextView>(R.id.tvsunrise).text = SimpleDateFormat("hh:mm a", Locale.ENGLISH).format(Date(sunrise*1000))
                findViewById<TextView>(R.id.tvsunset).text = SimpleDateFormat("hh:mm a", Locale.ENGLISH).format(Date(sunset*1000))
                findViewById<TextView>(R.id.tvwind).text = windSpeed
                findViewById<TextView>(R.id.tvpressure).text = pressure
                findViewById<TextView>(R.id.tvhumidity).text = humidity

                findViewById<ProgressBar>(R.id.pbloader).visibility = View.GONE
                findViewById<RelativeLayout>(R.id.rlmainContainer).visibility = View.VISIBLE
            }
            catch (e: Exception){
                findViewById<ProgressBar>(R.id.pbloader).visibility = View.GONE
                findViewById<TextView>(R.id.tverrorText).visibility = View.VISIBLE
            }
        }
    }
}