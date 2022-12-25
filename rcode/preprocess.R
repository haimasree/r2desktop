capitalize_input <- function(inputdir, outputdir, filetype){
  #' Capitalize arguments
  #'
  #' This function returns a custom statement comprising
  #' capitilzed input arguments
  #'
  #' @param inputdir Input directory
  #' @param outputdir Output directory
  #' @param filetype File type
  #
  inputdir <- toupper(inputdir)
  outputdir <- toupper(outputdir)
  filetype <- toupper(filetype)
  output <- paste("INPUT: ", inputdir, " OUTPUT: ", outputdir,
            " FILE TYPE: ", filetype,  sep = "")
  return(output)
}