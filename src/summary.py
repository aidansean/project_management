from project_module        import project_object

def summarise_html(write_wordpress, write_PHP):
    for p in projects:
        print p.github_repo_name
        prefix = 'projects_data/%s/%s/doc'%(p.folder_name,p.github_repo_name)
        if write_wordpress:
            file = open('%s/wordpress.txt'%prefix, 'w')
            file.write(p.wordpress_text()) ;
        if write_PHP:
            file = open('%s/project.php'  %prefix, 'w')
            file.write(p.PHP_text())

def links_table():
    lines = []
    lines.append('<table>')
    lines.append('  <tbody>')
    for p in projects:
        lines.append('    <tr>')
        lines.append('      <td>%s</td>'%p.title)
        lines.append('      <td>%s</td>'%p.name)
        link_lines = []
        link_lines.append('      <td>')
        for l in p.links:
            link_lines.append('        %s<br />'%l.html())
        link_lines.append('      </td>')
        lines.append('\n'.join(link_lines))
        lines.append('      <td><a href="%s">GitHub</a></td>'%p.github_uri())
        lines.append('    </tr>')
    lines.append('  </tbody>')
    lines.append('</table>')
    return'\n'.join(lines)

projects = []
from projects_data.aidansean.map91.project                      import p as map91
from projects_data.Physics.accelerator_future_prospects.project import p as future_prospects
from projects_data.LHCGames.aDetector.project                   import p as aDetector
from projects_data.aidansean.advent2012.project                 import p as advent2012
from projects_data.aidansean.alarm_clock.project                import p as alarm_clock
from projects_data.aidansean.apollonian.project                 import p as apollonian
from projects_data.aidansean.ascii_art.project                  import p as ascii_art
from projects_data.aidansean.boxer.project                      import p as boxer
from projects_data.aidansean.box_plotter.project                import p as box_plotter
from projects_data.aidansean.calendar.project                   import p as calendar
from projects_data.DataAnalysis.CERNOpenDataCMS.project         import p as CERNOpenDataCMS
from projects_data.aidansean.cipher.project                     import p as cipher
from projects_data.aidansean.circle_points.project              import p as circle_points
from projects_data.aidansean.citadel.project                    import p as citadel
from projects_data.aidansean.color_converter.project            import p as color_converter
from projects_data.aidansean.complex_polynomial.project         import p as complex_polynomial
from projects_data.aidansean.conway.project                     import p as conway
from projects_data.aidansean.crazy2014.project                  import p as crazy2014
from projects_data.aidansean.dailyfail.project                  import p as dailyfail
from projects_data.aidansean.dice.project                       import p as dice
from projects_data.aidansean.dice_game.project                  import p as dice_game
from projects_data.aidansean.drwho.project                      import p as drwho
from projects_data.aidansean.election.project                   import p as election
from projects_data.aidansean.errors.project                     import p as errors
from projects_data.Physics.EtaPhiMap.project                    import p as EtaPhiMap
from projects_data.aidansean.euler.project                      import p as euler
from projects_data.aidansean.explorer_game.project              import p as explorer_game
from projects_data.aidansean.eye_of_argon.project               import p as eye_of_argon
from projects_data.aidansean.feynman.project                    import p as feynman
from projects_data.aidansean.floorplan.project                  import p as floorplan
from projects_data.greasemonkey.greaseBox.project               import p as greaseBox
from projects_data.aidansean.guess_the_song.project             import p as guess_the_song
from projects_data.aidansean.hotel.project                      import p as hotel
from projects_data.aidansean.indigo.project                     import p as indigo
from projects_data.greasemonkey.i.project                       import p as i_greasemonkey
from projects_data.aidansean.image_fader.project                import p as image_fader
from projects_data.aidansean.image_morpher.project              import p as image_morpher
from projects_data.aidansean.insult.project                     import p as insult
from projects_data.aidansean.inverter.project                   import p as inverter
from projects_data.aidansean.iterated_path.project              import p as iterated_path
from projects_data.aidansean.keycode.project                    import p as keycode
from projects_data.aidansean.LGBT_map.project                   import p as LGBT_map
from projects_data.LHCGames.LHCDriver.project                   import p as LHCDriver
from projects_data.aidansean.links_pages.project                import p as links_pages
from projects_data.greasemonkey.LXR_tidy.project                import p as LXR_tidy
from projects_data.aidansean.mandelbrot.project                 import p as mandelbrot
from projects_data.aidansean.marathon.project                   import p as marathon
from projects_data.DataAnalysis.marriage.project                import p as marriage
from projects_data.aidansean.marble_hornets.project             import p as marble_hornets
from projects_data.aidansean.mastermind.project                 import p as mastermind
from projects_data.aidansean.maze.project                       import p as maze
from projects_data.aidansean.mssng_vwls.project                 import p as mssng_vwls
from projects_data.aidansean.multiplets.project                 import p as multiplets
from projects_data.aidansean.neuron.project                     import p as neuron
from projects_data.aidansean.painter.project                    import p as painter
from projects_data.aidansean.parodier.project                   import p as parodier
from projects_data.aidansean.pebbling.project                   import p as pebbling
from projects_data.aidansean.pi_estimation.project              import p as pi_estimation
from projects_data.aidansean.pixeler.project                    import p as pixeler
from projects_data.aidansean.platform_game.project              import p as platform_game
from projects_data.aidansean.project365.project                 import p as project365
from projects_data.Other.python_indenter.project                import p as python_indenter
from projects_data.aidansean.railway.project                    import p as railway
from projects_data.aidansean.recolourer.project                 import p as recolourer
from projects_data.aidansean.reflections.project                import p as reflections
from projects_data.Physics.ROOT_colors.project                  import p as ROOT_colors
from projects_data.aidansean.SCP.project                        import p as SCP
from projects_data.LHCGames.ScienceShiftSimulator.project       import p as ScienceShiftSimulator
from projects_data.Physics.ScramBuildEggs.project               import p as ScramBuildEggs
from projects_data.aidansean.sequences.project                  import p as sequences
from projects_data.aidansean.sliders.project                    import p as sliders
from projects_data.aidansean.SM_notes.project                   import p as SM_notes
from projects_data.aidansean.spectrum.project                   import p as spectrum
from projects_data.aidansean.symbols.project                    import p as symbols
from projects_data.aidansean.tetris.project                     import p as tetris
from projects_data.aidansean.transformer.project                import p as transformer
from projects_data.aidansean.tricolor.project                   import p as tricolor
from projects_data.LHCGames.trigger.project                     import p as trigger
from projects_data.aidansean.uncertainties_radar.project        import p as uncertainties_radar
from projects_data.aidansean.weird_youtube.project              import p as weird_youtube
from projects_data.aidansean.wolfram.project                    import p as wolfram
from projects_data.aidansean.youtube_thumbnailer.project        import p as youtube_thumbnailer

projects.append( map91                 )
projects.append( aDetector             )
projects.append( advent2012            )
projects.append( alarm_clock           )
projects.append( apollonian            )
projects.append( ascii_art             )
projects.append( boxer                 )
projects.append( box_plotter           )
projects.append( calendar              )
projects.append( CERNOpenDataCMS       )
projects.append( cipher                )
projects.append( circle_points         )
projects.append( citadel               )
projects.append( color_converter       )
projects.append( complex_polynomial    )
projects.append( conway                )
projects.append( crazy2014             )
projects.append( dailyfail             )
projects.append( dice                  )
projects.append( dice_game             )
projects.append( drwho                 )
projects.append( election              )
projects.append( errors                )
projects.append( EtaPhiMap             )
projects.append( euler                 )
projects.append( explorer_game         )
projects.append( eye_of_argon          )
projects.append( feynman               )
projects.append( floorplan             )
projects.append( future_prospects      )
projects.append( greaseBox             )
projects.append( guess_the_song        )
projects.append( hotel                 )
projects.append( indigo                )
projects.append( i_greasemonkey        )
projects.append( image_fader           )
projects.append( image_morpher         )
projects.append( insult                )
projects.append( inverter              )
projects.append( iterated_path         )
projects.append( keycode               )
projects.append( LHCDriver             )
projects.append( LGBT_map              )
projects.append( links_pages           )
projects.append( LXR_tidy              )
projects.append( mandelbrot            )
projects.append( marathon              )
projects.append( marriage              )
projects.append( marble_hornets        )
projects.append( mastermind            )
projects.append( maze                  )
projects.append( mssng_vwls            )
projects.append( multiplets            )
projects.append( neuron                )
projects.append( painter               )
projects.append( parodier              )
projects.append( pebbling              )
projects.append( pi_estimation         )
projects.append( pixeler               )
projects.append( platform_game         )
projects.append( project365            )
projects.append( python_indenter       )
projects.append( railway               )
projects.append( recolourer            )
projects.append( reflections           )
projects.append( ROOT_colors           )
projects.append( ScienceShiftSimulator )
projects.append( SCP                   )
projects.append( ScramBuildEggs        )
projects.append( sequences             )
projects.append( sliders               )
projects.append( SM_notes              )
projects.append( spectrum              )
projects.append( symbols               )
projects.append( tetris                )
projects.append( transformer           )
projects.append( tricolor              )
projects.append( trigger               )
projects.append( uncertainties_radar   )
projects.append( weird_youtube         )
projects.append( wolfram               )
projects.append( youtube_thumbnailer   )

sumamry_text = links_table()
f = open('table.html','w')
f.write(sumamry_text)

do_wordpress = True
do_PHP       = True
summarise_html(do_wordpress, do_PHP)

print
print len(projects) , 'projects'
