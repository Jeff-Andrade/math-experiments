getTable = function(data)
  
{

    histogram = hist(data, breaks = "Sturges", right = FALSE)
    
    intervalColumn = list()
    
    
    breaks = histogram$breaks
    frequencies = histogram$counts
    relativeFrequencies = round((frequencies/sum(frequencies)),3)
    relativeFrequenciesPercent = round(100*(frequencies/sum(frequencies)),3)
    
    for(i in 1:length(breaks)-1)
        
    {
        
        
        interval = paste(as.character(breaks[i]),"|-",as.character(breaks[i+1]))
            
        intervalColumn = append(intervalColumn,interval)
        
        
        
    }
    
    intervalColumn[1] = NULL
    
    df = data.frame("Intervals"=unlist(intervalColumn),"Absolute Frequency"=frequencies,
                "Relative Frequency"=relativeFrequencies,"Relative Frequency (%)"=relativeFrequenciesPercent)
    
    print(df)
    
   
    }
